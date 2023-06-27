from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from pharmacy.models import CustomUser, Producto, Almacen
from django.db.models import Count
from django.http import HttpResponse
from django.template import loader

import pdfkit
import base64

# Create your views here.

@user_passes_test(lambda user: user.groups.filter(name="supervisor").exists())
def dashboard(request):
    context = {}

     # Busqueda de registros por mes
    registros_por_mes = (
        Almacen.objects
        .values('month')
        .annotate(cantidad=Count('month'))
        .order_by('month')
    )

    # Crear un diccionario con los meses y las cantidades
    registros_por_mes_dict = {}
    for registro in registros_por_mes:
        mes = registro['month']
        cantidad = registro['cantidad']
        registros_por_mes_dict[mes] = cantidad

    # Agregar 0 para los meses sin registros
    for mes in range(1, 13):
        if mes not in registros_por_mes_dict:
            registros_por_mes_dict[mes] = 0

    registros_por_mes_dict = {k: v for k, v in registros_por_mes_dict.items() if k is not None}
    registros_por_mes_list = [registros_por_mes_dict.get(mes, 0) for mes in range(1, 13)]

    context['total_month'] = registros_por_mes_list
    context['users'] = CustomUser.objects.count()
    context['warehouses'] = Almacen.objects.count()
    context['products'] = Producto.objects.filter(disponibilidad=True).count()
    return render(request, 'dashboard.html', context)

def create_pdf(request):

    almacen = Almacen.objects.all()
    
    html = loader.render_to_string('pdf.html', {'almacen':almacen})
    wkhtmltopdf_path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)
    output= pdfkit.from_string(html, False, configuration=config)
    response = HttpResponse(content_type="application/pdf")
    response.write(output)

    filename = "Reporte_de_Almacen.pdf"

    response['Content-Disposition'] = 'attachment; filename="' + filename + '"'
    return response
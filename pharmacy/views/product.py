from django.shortcuts import render
from pharmacy.models import Producto
from django.shortcuts import get_object_or_404
from django.db import IntegrityError

# Create your views here.
def product(request):
    context = {}
    context['productos'] = Producto.objects.all()
    return render(request, 'product.html', context)

def create_product(request):
    if request.method == 'POST':
        nombre_producto = request.POST['nombre']
        precio_compra = request.POST['precioCompra']
        precio_venta = request.POST['precioVenta']
        disponibilidad = request.POST['disponibilidad']
        descripcion = request.POST['descripcion']
        imagen = request.FILES.get('imagen')

        producto = Producto(
            nombre_producto=nombre_producto,
            precio_compra=precio_compra,
            precio_venta=precio_venta,
            disponibilidad=bool(int(disponibilidad)),
            descripcion=descripcion,
            imagen=imagen
        )
        producto.save()

        return redirect('product')

    return render(request, 'create_product.html')

def edit_product(request,pk):
    context={}
    if request.method == 'POST':
        try:
            producto = Producto.objects.get(id=pk)
            imagen = request.FILES.get('imagen')

            # Actualizar los campos del producto con los valores recibidos del formulario
            producto.nombre_producto = request.POST.get('nombre')
            producto.precio_compra = request.POST.get('precioCompra')
            producto.precio_venta = request.POST.get('precioVenta')
            producto.disponibilidad = bool(int(request.POST.get('disponibilidad')))
            producto.descripcion = request.POST.get('descripcion')
            if imagen != None:
                producto.imagen = imagen

            # Guardar el producto actualizado
            producto.save()

        except IntegrityError:
            return redirect('product')


        return redirect('product')
    elif request.method == 'GET':
        context['producto'] = get_object_or_404(Producto, id=pk)
        context['producto'].precio_compra = str(context['producto'].precio_compra)
        context['producto'].precio_venta = str(context['producto'].precio_venta)
        return render(request, 'edit_product.html', context)
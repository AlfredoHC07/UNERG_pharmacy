from django.shortcuts import render, redirect
from pharmacy.models import Almacen, Producto
from django.shortcuts import get_object_or_404
from django.db import IntegrityError

def warehouse(request):
    context = {}
    context['registros'] = Almacen.objects.all()
    return render(request, 'warehouse.html', context)

def create_warehouse(request):
    context = {}

    if request.method == 'POST':
        producto_id = int(request.POST['producto'])
        cantidad_producto = request.POST['cantidad_producto']
        producto = Producto.objects.get(id=producto_id)

        warehouse = Almacen(
            producto=producto,
            cantidad_producto=cantidad_producto
        )
        warehouse.save()

        return redirect('warehouse')
    elif request.method == 'GET':
        context['productos'] = Producto.objects.filter(disponibilidad=True)
        return render(request, 'create_warehouse.html', context)

def edit_warehouse(request,pk):
    context = {}
    almacen = Almacen.objects.get(id=pk)

    if request.method == 'POST':
        producto_id = int(request.POST.get('producto'))
        cantidad_producto = request.POST.get('cantidad_producto')
        almacen.producto = Producto.objects.get(id=producto_id)
        almacen.cantidad_producto = cantidad_producto
        almacen.cantidad_producto_vendidos = request.POST.get('cantidad_producto_vendidos')
        almacen.save()

    elif request.method == 'GET':
        context['productos'] = Producto.objects.filter(disponibilidad=True)
        context['registro'] = almacen
        return render(request, 'edit_warehouse.html', context)
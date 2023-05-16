from django.shortcuts import render, redirect
from pharmacy.models import Producto

# Create your views here.
def product(request):
    context = {}
    context['productos'] = Producto.objects.all()
    return render(request, 'product.html', context)
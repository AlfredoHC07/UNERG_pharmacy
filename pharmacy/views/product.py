from django.shortcuts import render, redirect
from .login import login_required
from pharmacy.models import Producto

# Create your views here.
@login_required
def product(request):
    context = {}
    context['productos'] = Producto.objects.all()
    return render(request, 'product.html', context)
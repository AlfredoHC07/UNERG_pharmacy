from django.shortcuts import render, redirect
from pharmacy.models import Almacen

# Create your views here.
def index(request):
    return redirect('login')
    
def home(request):
    context = {}
    context['registros'] = Almacen.objects.all()
    return render(request,'home.html', context)
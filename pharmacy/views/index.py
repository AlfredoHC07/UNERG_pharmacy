from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return redirect('home')
    
def home(request):
    return redirect('login')
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from pharmacy.models import CustomUser
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper

def signout(request):
    logout(request)
    return redirect('home')

def signup(request):
    autenticate = True

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'autenticate': autenticate
        })
    else:
        try:
            user = CustomUser.objects.create_user(
                username=request.POST['username'],
                first_name=request.POST['Name'],
                last_name=request.POST['LastName'],
                email=request.POST['Email'], 
                password=request.POST['Password'],
                rif=request.POST['Dni'],
                phone=request.POST['Phone'],
            )
            user.save()
            login(request, user)
            return redirect('dashboard')

        except IntegrityError:
            return render(request, 'signup.html', {
                'form': UserCreationForm,
                'error': 'El usuario ya existe',
                'autenticate': autenticate
            })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Las claves no coinciden',
            'autenticate': autenticate
        })

def signin(request):
    autenticate = True

    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        
        if user is None:
            return render(request, 'login.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o clave es incorrecto'
            })
        else:
            login(request, user)
            return redirect('dashboard')


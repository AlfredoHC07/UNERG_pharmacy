from django.shortcuts import render, redirect
from pharmacy.models import CustomUser
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Group
from django.db import IntegrityError

def signout(request):
    logout(request)
    return redirect('home')

def signup(request):
    context = {}
        
    if request.user.is_authenticated:
            return redirect("dashboard")

    if request.method == 'GET':
        return render(request, 'signup.html')
    
    elif request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = CustomUser.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                user = authenticate(username= request.POST['username'], password = request.POST['password1'])
                
                supervisor_group = Group.objects.get(name="supervisor")
                user.groups.add(supervisor_group)
                
                if user is not None:
                    login(request, user)
                    return redirect('dashboard')
                else:
                    error = 'Error de autenticación'
                    
            except IntegrityError:
                
                context["error"] = 'El usuario ya existe'
                return render(request, 'signup.html', context)
        else:
            context["error"] = 'Las claves no coinciden'
            return render(request, 'signup.html', context)


def signin(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        
        if user is None:
            return render(request, 'login.html', {
                'error': 'Usuario o clave es incorrecto'
            })
        else:
            login(request, user)
            return redirect('dashboard')


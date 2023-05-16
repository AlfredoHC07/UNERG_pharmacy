from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from pharmacy.models import CustomUser
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


# def login_required(view_func): DUDOSO
#     def wrapper(request, *args, **kwargs): DUDOSO
#         if not request.user.is_authenticated: DUDOSO
#             return redirect('login') DUDOSO
#         return view_func(request, *args, **kwargs) DUDOSO
#     return wrapper DUDOSO

def signout(request):
    logout(request)
    return redirect('home')




    if request.method == 'GET':
        form = UserCreationForm()
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('dashboard')

    return render(request, 'signup.html', {'form': form})

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
                print("hola xd")
                user.save()
                print(user)
                user = authenticate(username= request.POST['username'], password = request.POST['password1'])
                
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
    autenticate = True

    if request.method == 'GET':
        return render(request, 'login.html')
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


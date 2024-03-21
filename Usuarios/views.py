from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate, logout

from django.contrib import messages

from .forms import RegisterForm, LoginForm

def register_view(request):
    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = form.save()
        messages.success(request, 'Usuario registrado con éxito')

        if user:
            login(request, user)
            return redirect('Notas:index')

    return render(request, 'register.html', {
        'form':form
    })

def login_view(request):
    form = LoginForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('Notas:index')
        else:
            messages.error(request, 'Nombre de usuario y contraseña incorrecta')

    return render(request, 'login.html', {
      'form':form
    })

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada con éxito')
    return redirect('Usuarios:login')
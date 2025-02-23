from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


def inicioSesion(request):
    return render(request, 'login.html')


def login_usuario(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Verificamos si el usuario existe y la contraseña es correcta
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Iniciar sesión
            return redirect('/inicio/')  # Redirigir a la página de inicio
        else:
            return render(request, "login.html", {"error_message": "Usuario o contraseña incorrectos"})

    return render(request, "login.html")

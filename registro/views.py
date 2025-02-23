from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import Usuario


# Create your views here.
def formulario(request):
    return render(request, 'registro.html')

from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Solo temporalmente para pruebas; después usa el token CSRF en el formulario
def registro_usuario(request):
    if request.method == "POST":
        print(request.POST)  # Imprime los datos recibidos en la terminal
        
        nombre = request.POST.get("nombre-personal")
        username = request.POST.get("usuario-nombre")
        edad = request.POST.get("usuario-edad")
        email = request.POST.get("usuario-correo")  # Corregido
        password = request.POST.get("usuario-pass")

        if not (nombre and username and edad and email and password):
            return HttpResponse("Faltan campos obligatorios", status=400)

        nuevo_usuario = Usuario(nombre=nombre, username=username, edad=edad, email=email, password=password)
        nuevo_usuario.save()
        return redirect('/inicio/')

    return HttpResponse("Método no permitido", status=405)

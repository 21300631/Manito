from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import Usuario
import re

# Create your views here.
def formulario(request):
    return render(request, 'registro.html')

from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Larisa, esto es para pruebas, cuando se haga el login de verdad, se quita
def registro_usuario(request):
    if request.method == "POST":
        print(request.POST)  
        
        nombre = request.POST.get("nombre-personal")
        username = request.POST.get("usuario-nombre")
        edad = request.POST.get("usuario-edad")
        email = request.POST.get("usuario-correo")  
        password = request.POST.get("usuario-pass")
        password2 = request.POST.get("usuario-pass2")

        context = {
            'nombre': nombre,
            'username': username,
            'edad': edad,
            'email': email,
        }

        
        if not (nombre and username and edad and email and password):
            context['error'] = 'Faltan campos obligatorios'
            return render(request, 'registro.html', context)
        
        if Usuario.objects.filter(username=username).exists():
            context['error'] = 'El usuario ya existe'
            return render(request, 'registro.html', context)
        
        if len(password) < 8:
            context['error'] = 'La contraseña debe tener al menos 8 caracteres'
            return render(request, 'registro.html', context)
        if not re.search("[a-z]", password):
            context['error'] = 'La contraseña debe tener al menos una letra minúscula'
            return render(request, 'registro.html', context)
        if not re.search("[A-Z]", password):
            context['error'] = 'La contraseña debe tener al menos una letra mayúscula'
            return render(request, 'registro.html', context)
        if not re.search("[0-9]", password):
            context['error'] = 'La contraseña debe tener al menos un número'
            return render(request, 'registro.html', context)

        if password != password2:
            return render(request, 'registro.html', {'error': 'Las contraseñas no coinciden'})

        nuevo_usuario = Usuario(nombre=nombre, username=username, edad=edad, email=email, password=password)
        nuevo_usuario.save()
        return redirect('/inicio/')

    return HttpResponse("Método no permitido", status=405)




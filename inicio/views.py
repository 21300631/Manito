from django.shortcuts import render

# Create your views here.
def inicioSesion(request):
    return render(request, 'inicio.html', {'mensaje': 'Haz iniciado sesión'})	

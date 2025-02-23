from django.urls import path
from .views import inicioSesion, login_usuario

urlpatterns = [
    path('', inicioSesion, name='inicioSesion'),
    path('login/', login_usuario, name="login")
]
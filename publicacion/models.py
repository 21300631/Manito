from django.db import models
from registro.models import Profile
from .storages import ImageStorage  # Mantén esta línea

# Create your models here.
class Publicacion(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.TextField()
    hashtags = models.CharField(max_length=100)  # Añade max_length
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(storage=ImageStorage(), upload_to='posts/', blank=True, null=True)  # Mantén este campo
    usuario = models.ForeignKey(Profile, on_delete=models.SET_DEFAULT, default='usuario_eliminado')

    def __str__(self):
        return self.titulo
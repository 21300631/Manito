from django.db import models
from registro.models import Usuario

# Create your models here.
class Publicacion(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.TextField()
    hashtags = models.CharField()
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_DEFAULT, default='usuario_eliminado')
    
    def __str__(self):
        return self.titulo
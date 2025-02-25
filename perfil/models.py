from django.db import models
from registro.models import Usuario


# Create your models here.
class Insignia(models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='insignias/')
    
    def __str__(self):
        return self.nombre
    
class Logro(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    insignia = models.ForeignKey(Insignia, on_delete=models.CASCADE)
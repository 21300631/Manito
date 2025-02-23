from django.db import models

class Usuario(models.Model):
    username = models.CharField(max_length=50, unique=True, default='primer_usuario')
    nombre = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=8)
    edad = models.IntegerField()
    racha = models.IntegerField(default=0)
    imagen = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.username

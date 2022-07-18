
from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre = models.CharField(max_length=40)
    parentezco = models.CharField(max_length=40)
    edad = models.IntegerField(max_length=40)
    fechaDeNacimiento = models.DateField(max_length=40)
    trabajador = models.BooleanField()
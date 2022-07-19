
from django.db import models

# Create your models here.

class Familiar(models.Model):

    nombre = models.CharField(max_length=40)
    parentezco = models.CharField(max_length=40)
    edad = models.IntegerField()
    fechaDeNacimiento = models.DateField()
    trabajador = models.BooleanField()
    
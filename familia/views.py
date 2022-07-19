from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from datetime import date, datetime
from django.template import loader
from familia.models import Familiar
# Create your views here.


def agregarfamiliar(request, nombre, parentezco, edad, fechaDeNacimiento, trabajador):
    pariente = Familiar(nombre = nombre, parentezco = parentezco, edad= edad, fechaDeNacimiento = fechaDeNacimiento, trabajador = trabajador)
    pariente.save()

    return HttpResponse(f"""
    <p> nombre: {pariente.nombre} - parentezco: {pariente.parentezco} - edad: {pariente.edad} - fechaDeNacimiento: {pariente.fechaDeNacimiento} - trabaja: {pariente.trabajador} - AGREGADO </p>
    """)

def inicio(request):
    return HttpResponse(f"""
    <p>Esto es un precario inicio.</p>
    """)


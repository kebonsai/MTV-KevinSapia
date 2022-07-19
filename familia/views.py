from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from familia.models import Familiar
# Create your views here.


def agregarfamiliar(self, nom, parent, ed, fechaDeNac, trabaj):
    pariente = Familiar(nombre = nom, parentezco = parent, edad= ed, fechaDeNacimiento = fechaDeNac, trabajador = trabaj)
    pariente.save()
    lista = [nom,parent,ed,fechaDeNac,trabaj]

    return render(self,"agregarfamiliar.html",{"nuevofamiliar": lista})

    #return HttpResponse(f"""
    #<h1>Agregando familiar: </h1>
    #<p>Agregando a la base de datos nombre: {pariente.nombre} - parentezco: {pariente.parentezco} - edad: {pariente.edad} - fechaDeNacimiento: {pariente.fechaDeNacimiento} - trabaja: {pariente.trabajador} - AGREGADO </p>
    #""")

def listarfamiliares(self):
    lista = Familiar.objects.all

    return render(self,"lista_familiares.html",{"lista_familiares": lista})

def inicio(request):
    return HttpResponse(f"""
    <h1>Esto es un precario inicio.</h1>
    """)


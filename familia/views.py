from django.http import HttpResponse
from django.shortcuts import render
from familia.models import Familiar
# Create your views here.

#ésta funsión agarra los parámetros y los usa para crear un pariente usando la clase Familiar.
#luego verifica el valor proporcionado por la funsión "existefamiliar"
#y en base a eso guarda o no el pariente en la base de datos. en ambos casos muestra un render diferente.
def agregarfamiliar(request, nom, parent, ed, fechaDeNac, trabaj):
    pariente = Familiar(nombre = nom, parentezco = parent, edad= ed, fechaDeNacimiento = fechaDeNac, trabajador = trabaj)
    if not existefamiliar(pariente.nombre):
        pariente.save()
        return render(request,"agregarfamiliar.html", {"nuevofamiliar": pariente})
    return render(request,"familiarexistente.html",{"nuevofamiliar": pariente})

#Cree una funsión que revisa si ya existe el nombre en la base de datos y devuelve un valor booleano
def existefamiliar(nombre):
    return Familiar.objects.filter(nombre=nombre).exists()
#funsión utilizada para listar los objetos dentro de la base de datos, de modo que puedan convertirse facilmente en un diccionario 
#para luego pasarselo al render. el template muestra las entradas guardadas en la base de datos.
def listarfamiliares(self):
    lista = Familiar.objects.all

    return render(self,"lista_familiares.html",{"lista_familiares": lista})
#simplemente muestra la pagina principal.
def inicio(request):
    
    return render(request,"inicio.html",{})



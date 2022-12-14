from django.shortcuts import render
from .models import Familiares
from django.http import HttpResponse

# Create your views here.

def Familiares(request):

    familiar= Familiares(nombre="Alejandro", parentezco="Hermano", edad=33, fecha_nacimiento=13-10-1989)
    familiar.save()
    cadena_texto=f"familiar guardado: {familiar.nombre}, {familiar.parentezco}, {familiar.edad}, {familiar.fecha_nacimiento}"
    return HttpResponse(cadena_texto)

# -*- coding: utf-8 -*-

from alumnos.models import Materia
from django.shortcuts import render_to_response

# La creación de materias por ahora sólo se realiza desde la interfaz
# de administración.

def lista(peticion):
    lista_materias = Materia.objects.all().order_by('nombre')#[:10]
    return render_to_response('materia/lista.html',
                              {'lista_materias': lista_materias})

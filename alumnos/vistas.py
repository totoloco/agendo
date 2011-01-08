# -*- coding: utf-8 -*-

from alumnos.models import Materia
from django.shortcuts import render_to_response
from django.template import RequestContext

# La creación de materias por ahora sólo se realiza desde la interfaz
# de administración.

def render_response(peticion, *args, **kwargs):
    kwargs['context_instance'] = RequestContext(peticion)
    return render_to_response(*args, **kwargs)

def lista(peticion):
    lista_materias = Materia.objects.all().order_by('nombre')#[:10]
    return render_response(peticion,
                           'materia/lista.html',
                           {'lista_materias': lista_materias})

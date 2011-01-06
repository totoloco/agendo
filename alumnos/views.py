# -*- coding: utf-8 -*-
from django.template import Context, loader
from alumnos.models import Materia
from django.http import HttpResponse

# la creación de materias por ahora sólo se realiza desde el admin

def index(request):
    materia_list = Materia.objects.all().order_by('nombre')#[:10]
    t = loader.get_template('materia/index.html')
    c = Context({
        'materia_list': materia_list,
    })
    return HttpResponse(t.render(c))

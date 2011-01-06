# -*- coding: utf-8 -*-
from django.template import Context, loader
from alumnos.models import Subject
from django.http import HttpResponse

# la creación de materias por ahora sólo se realiza desde el admin

def index(request):
    subject_list = Subject.objects.all().order_by('name')#[:10]
    t = loader.get_template('subject/index.html')
    c = Context({
        'subject_list': subject_list,
    })
    return HttpResponse(t.render(c))

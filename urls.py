# -*- coding: utf-8 -*-

from settings import *
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    # Descomentá la siguiente línea para activar la documentación de la
    # interfaz de administración:
    #(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # SOLO PARA DEPURACIÓN Y DESARROLLO:
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT}),
    (r'^', include('alumnos.urls')),
)


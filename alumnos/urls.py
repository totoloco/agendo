# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$',        'alumnos.vistas.lista'),
    (r'^cuentas/', include('registration.urls')),
)

#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from django.core.management import execute_manager

try:
    import settings # Se asume que está en el directorio del proyecto.
except ImportError:
    import sys
    sys.stderr.write('''\
Error: no se puede encontrar el archivo “settings.py” en el directorio que
contiene “%s”. Parece que te faltó configurar cosas.  Vas a tener que
ejecutar ”django-admin.py”, pasándole tu módulo settings.  (Si el archivo
“settings.py” efectivamente existe, está causando un ImportError de alguna
manera.)
''' % __file__)
    sys.exit(1)

if __name__ == '__main__':
    execute_manager(settings)

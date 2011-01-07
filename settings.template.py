# -*- coding: utf-8 -*-
'''Configuración de Django para el proyecto Agendo.'''

# INSTRUCCIONES:
# Renombrá este archivo a “settings.py” y reemplazá todas las ocurriencias de
# “USUARIO” en las rutas por tu nombre de usuario del sistema operativo.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Tu Nombre', 'tu_correo@dominio.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        # Motor de base de datos a usar. Podés cambiar ``sqlite3`` por
        # ``postgresql_psycopg2``, ``postgresql``, ``mysql`` u ``oracle``.
        'ENGINE': 'django.db.backends.sqlite3',
        # Nombre de la base de datos o ruta al archivo de base de datos si
        # usás sqlite3.
        'NAME': '/home/USUARIO/builds/agendo/agendo.sqlite',
        # Usuario de la base de datos. No se usa con sqlite3.
        'USER': '',
        # Contraseña de la base de datos. No se usa con sqlite3.
        'PASSWORD': '',
        # Dirección del servidor donde está alojada la base de datos. No se
        # usa con sqlite3.
        'HOST': '',
        # Puerto de dicho servidor. No se usa con sqlite3.
        'PORT': '',
    }
}

# Zona horaria local para esta instalación. Las posibles opciones se pueden
# encontrar acá: http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# aunque no todas pueden estar disponibles en todos los sistemas operativos.
# En sistemas Unix, un valor None hace que Django use el mismo huso horario
# que el sistema operativo.
# Si estás bajo un entorno Windows, tenés que hacer coincidir este parámetro
# con el huso horario de tu sistema.
TIME_ZONE = 'America/Argentina/Ushuaia'

# Código de idioma para esta instalación. Las opciones posibles se pueden
# encontrar acá: http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es-AR'

SITE_ID = 1

# Si lo establecés como False, Django va a hacer algunas optimizaciones para
# no cargar la maquinaria de internacionalización.
USE_I18N = True

# Si lo establecés como False, Django no va a formatear las fechas, números y
# calendarios de acuerdo con la “locale” actual.
USE_L10N = True

# Ruta absoluta del sistema de archivos al directorio que tendrá los archivos
# que suban los usuarios. Ejemplo: “/home/media/media.lawrence.com/”.
MEDIA_ROOT = ''

# Dirección URL que maneja los medios servidos desde MEDIA_ROOT. Asegurate de
# agregar una barra al final si hay un componente de ruta (opcional en otros
# casos). Ejemplos: “http://media.lawrence.com”, “http://ejemplo.com/media/”.
MEDIA_URL = ''

# Prefijo de direcciones URL para medios de la administración (CSS, JavaScript
# e imágenes). Asegurate de agregar una barra al final. Ejemplos:
# “http://foo.com/media/”, “/media/”.
ADMIN_MEDIA_PREFIX = '/media/'

# Hacela única y no la compartas con nadie.
SECRET_KEY = '=$3k#h2)^o7*^j_37h58f+%ix%i*&+b7wyot+7$#x6l7e+e2v!'

# Lista de “callables” que saben cómo importar plantillas desde varias fuentes.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'agendo.urls'

TEMPLATE_DIRS = (
    # Poné cadenas de texto acá, como “/home/html/django_plantillas” o
    # “C:/www/django/plantillas”.
    # Usá siempre barras sin invertir, incluso en Windows.
    # No te olvides de usar rutas absolutas, no relativas.
    '/home/USUARIO/builds/agendo/plantillas'
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    # Descomentá la siguiente línea para activar la interfaz de 
    # administración:
    'django.contrib.admin',
    # Descomentá la siguiente línea para activar la documentación de la
    # interfaz de administración:
    #'django.contrib.admindocs',
    # Apliación de registro de usuarios:
    'registration',
    # APLICACIÓN PRINCIPAL:
    'alumnos',
)

LOGIN_REDIRECT_URL = '/'

ACCOUNT_ACTIVATION_DAYS = 5

STATIC_ROOT = '/home/USUARIO/builds/agendo/media'

EMAIL_HOST = 'smtp.correo.com'
EMAIL_HOST_USER = 'correo@correo.com'
EMAIL_HOST_PASSWORD = 'clave'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

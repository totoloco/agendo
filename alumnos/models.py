# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

class Materia(models.Model):
    
    nombre = models.CharField(max_length = 255)
    profesores = models.CharField(max_length = 255)
    correos_de_profesores = models.CharField(max_length = 255)
    url = models.CharField(max_length = 255)
    usuario = models.ForeignKey(User)
    # Opcionales para agregar: is_active, created, updated,
    # user_id (el usuario que creó la materia).
    
    def __unicode__(self):
        return self.nombre

# -*- coding: utf-8 -*-
from django.db import models

# subject == materia
class Subject(models.Model):
    name = models.CharField(max_length=255)
    teachers = models.CharField(max_length=255)
    teacher_emails = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    # opcionales para agregar: is_active, created, updated, user_id (el usuario que creó la materia)

    def __unicode__(self):
        return self.name

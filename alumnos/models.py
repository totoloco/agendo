from django.db import models

# subject == materia
class Subject(models.Model):
  name = models.CharField(max_length=255)
  teachers = models.CharField(max_length=255)
  teacher_emails = models.CharField(max_length=255)
  url = models.CharField(max_length=255)
  # opcionales para agregar: is_active, created, updated, user_id (el usuario que creO la materia)

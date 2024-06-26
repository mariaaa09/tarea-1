from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=100, null=True)
    asignatura = models.CharField(max_length=100, null=True)

class Estudiante(models.Model):
    nombre = models.CharField(max_length=200, null=True)
    apellidos = models.CharField(max_length=200, null=True)
    fecha_nacimiento = models.DateTimeField(null=True)
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING, null=True)
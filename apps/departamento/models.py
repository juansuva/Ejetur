from django.db import models

class Departamento(models.Model):
	nombre=models.CharField(max_length=30)
	descripcion=models.CharField(max_length=30)


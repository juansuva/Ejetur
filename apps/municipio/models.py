from django.db import models

from apps.departamento.models import Departamento

class Municipio(models.Model):
	nombre=models.CharField(max_length=30)
	iddepartamento=models.OneToOneField(Departamento, null=True, blank=True, on_delete=models.CASCADE)
	descripcion=models.CharField(max_length=100)
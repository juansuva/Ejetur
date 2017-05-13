from django.db import models
from apps.generos.models import Genero
from apps.interes.models import Interes

# Create your models here.
class Persona(models.Model):
	nombre = models.CharField(max_length=50)
	apellido =models.CharField(max_length=20)
	direccion =models.TextField(max_length=50)
	telefono =models.IntegerField()
	celular =models.IntegerField()
	fecha_incripcion = models.DateField(null=True)
	prioridad =models.IntegerField(null=True)
	email =models.EmailField(blank=True)
	edad =models.IntegerField()
	sexo =models.OneToOneField(Genero, null=True , blank=True, on_delete=models.CASCADE)
	estado =models.IntegerField()
	solicitud =models.IntegerField()
	password =models.CharField(max_length=30)
	intereses =models.ForeignKey(Interes, null=True, blank=True, on_delete=models.CASCADE)

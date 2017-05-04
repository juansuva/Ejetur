from django.db import models

# Create your models here.
class Persona(models.Model):
	nombre = models.CharField(max_length=50)
	apellido =models.CharField(max_length=20)
	direccion =models.TextField(max_length=50)
	telefono =models.IntegerField()
	celular =models.IntegerField()
	fecha_incripcion = models.DateField()
	prioridad =models.IntegerField()
	email =models.EmailField()
	edad =models.IntegerField()
	sexo =models.CharField(max_length=10)
	estado =models.IntegerField()
	solicitud =models.IntegerField()
	password =models.CharField(max_length=30)
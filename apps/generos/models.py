from django.db import models

# Create your models here.
class Genero(models.Model):
	tipogenero=models.CharField(max_length=20)
	
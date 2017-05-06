from django.db import models

# Create your models here.
class Interes(models.Model):
	tipointeres=models.CharField(max_length=20)
	descripcion=models.CharField(max_length=50)


	def __str__(self):
		return '{}'.format(self.tipointeres)
from django.db import models

# Create your models here.
class Genero(models.Model):
	tipogenero=models.CharField(max_length=20)

	def __str__(self):
		return '{}'.format(self.tipogenero)
	
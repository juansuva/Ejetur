from django.db import models

# Create your models here.

class Tipo_usuario(models.Model):
	tipo_user=models.CharField(max_length=20)
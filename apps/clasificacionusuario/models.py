from django.db import models
from apps.persona.models import Persona
from apps.tipo_usuario.models import Tipo_usuario
# Create your models here.
class Clasificacionusuario(models.Model):
	
	persona=models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
	tipouser=models.ForeignKey(Tipo_usuario, null=True, blank=True, on_delete=models.CASCADE)
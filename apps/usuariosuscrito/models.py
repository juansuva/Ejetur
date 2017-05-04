from django.db import models

from apps.persona.models import Persona
from apps.clasificacionusuario.models import Clasificacionusuario

class Usuariosuscrito(models.Model):
	persona=models.OneToOneField(Persona, null=True, blank=True, on_delete=models.CASCADE)
	clasificacion=models.OneToOneField(Clasificacionusuario, null=True, blank=True, on_delete=models.CASCADE)

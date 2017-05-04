from django.db import models

from apps.persona.models import Persona
from apps.municipio.models import Municipio
from apps.interes.models import Interes

# Create your models here.
class Administradores(models.Model):
	usuario=models.OneToOneField(Persona, null=True, blank=True, on_delete=models.CASCADE)
	municipio=models.OneToOneField(Municipio, null=True, blank=True, on_delete=models.CASCADE)
	interes=models.OneToOneField(Interes, null=True, blank=True, on_delete=models.CASCADE)

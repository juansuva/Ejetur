from django.db import models

# Create your models here.
from apps.persona.models import Persona


class root(Persona):
	idroot=models.IntegerField()
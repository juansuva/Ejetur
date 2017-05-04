from django.contrib import admin

# Register your models here.
from apps.persona.models import Persona
from apps.municipio.models import Municipio
from apps.interes.models import Interes
from apps.administrador.models import Administradores

admin.site.register(Administradores)

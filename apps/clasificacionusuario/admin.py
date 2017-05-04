from django.contrib import admin

# Register your models here.
from apps.persona.models import Persona
from apps.tipo_usuario.models import Tipo_usuario
from apps.clasificacionusuario.models import Clasificacionusuario


admin.site.register(Clasificacionusuario)

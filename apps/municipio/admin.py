from django.contrib import admin

# Register your models here.
from apps.departamento.models import Departamento
from apps.municipio.models import Municipio


admin.site.register(Municipio)

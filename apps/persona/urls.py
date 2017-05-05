from django.conf.urls import url
from django.contrib import admin
from apps.persona.views import index,persona_view


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^registro$', persona_view,  name='persona_registro'),
]

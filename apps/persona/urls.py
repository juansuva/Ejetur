from django.conf.urls import url
from django.contrib import admin
from apps.persona.views import index,persona_view,index2


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^2$', index2, name='index2'),
    url(r'^registro$', persona_view,  name='persona_registro'),
]

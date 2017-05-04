from django.conf.urls import url
from django.contrib import admin
from apps.persona.views import index

urlpatterns = [
    url(r'^$', index),
]

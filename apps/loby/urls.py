from django.conf.urls import url
from django.contrib import admin
from apps.loby.views import InicioView

urlpatterns = [
    url(r'^$', InicioView.as_view(), name='inicio'),
]

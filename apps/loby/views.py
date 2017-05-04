from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


from django.views.generic.base import TemplateView
# Create your models here.
class InicioView(TemplateView):
	template_name="loby/index.html"

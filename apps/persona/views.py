from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.persona.forms import PersonaForms
from django.core.urlresolvers import reverse



def index(request):
	return HttpResponse("Index")


def persona_view(request):
	if request.method == 'POST':
		form=PersonaForms(request.POST)
		if form.is_valid():
			form.save()
			reverse
		return redirect('personal:index')
	else:
		form=PersonaForms()

	return render(request,'ejetur/persona_form.html',{'form':form})	



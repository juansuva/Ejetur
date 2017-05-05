from django import forms

from apps.persona.models import Persona
from apps.generos.models import Genero


class PersonaForms(forms.ModelForm):

	class Meta():
		model=Persona

		fields=[
			'nombre',
			'apellido',
			'direccion',
			'telefono',
			'celular',
			'fecha_incripcion',
			'prioridad',
			'email',
			'edad',
			'sexo',
			'estado',
			'solicitud',
			'password',
			'intereses',
		]

		labels={
			'nombre': 'Nombre',
			'apellido': 'Apellido',
			'direccion': 'Direccion',
			'telefono': 'Telefono',
			'celular': 'Celular',
			'fecha_incripcion': 'Fecha_incripcion',
			'prioridad': 'Prioridad',
			'email': 'Email',
			'edad': 'Edad',
			'sexo': 'Sexo',
			'estado': 'Estado',
			'solicitud': 'Solicitud',
			'password': 'Password',
			'intereses': 'Intereses',

		}

		widgets={
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'apellido': forms.TextInput(attrs={'class':'form-control'}),
			'direccion': forms.TextInput(attrs={'class':'form-control'}),
			'telefono': forms.TextInput(attrs={'class':'form-control'}),
			'celular': forms.TextInput(attrs={'class':'form-control'}),
			'fecha_incripcion': forms.TextInput(attrs={'class':'form-control'}),
			'prioridad':forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.TextInput(attrs={'class':'form-control'}),
			'edad': forms.TextInput(attrs={'class':'form-control'}),
			'sexo': forms.TextInput(attrs={'class':'form-control'}),
			'estado':forms.TextInput(attrs={'class':'form-control'}),
			'solicitud':forms.TextInput(attrs={'class':'form-control'}),
			'password':forms.TextInput(attrs={'class':'form-control'}),
			'intereses':forms.TextInput(attrs={'class':'form-control'}),
		}
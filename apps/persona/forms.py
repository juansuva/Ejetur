from django import forms

from apps.persona.models import Persona
from apps.generos.models import Genero
from apps.interes.models import Interes


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
			'telefono': forms.NumberInput(attrs={'class':'form-control'}),
			'celular': forms.NumberInput(attrs={'class':'form-control'}),
			'fecha_incripcion': forms.DateInput(attrs={'class':'form-control'}),
			'prioridad':forms.NumberInput(attrs={'class':'form-control'}),
			'email': forms.EmailInput(attrs={'class':'form-control'}),
			'edad': forms.NumberInput(attrs={'class':'form-control'}),
			'sexo': forms.Select(attrs={'class':'form-control'}),
			'estado':forms.TextInput(attrs={'class':'form-control'}),
			'solicitud':forms.NumberInput(attrs={'class':'form-control'}),
			'password':forms.NumberInput(attrs={'class':'form-control'}),
			'intereses':forms.CheckboxSelectMultiple(attrs={'class':'form-control'}),
		}
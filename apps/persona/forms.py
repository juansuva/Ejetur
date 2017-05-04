from django import forms

from apps.persona.model import Persona


class PersonaForms(forms.ModelForm):

	class Meta():
		model=Persona

		fields=[
			'nombre',
			'apellido',
			'direccion',
			'telefono',
			'celular',
			'fecha_inscripcion',
			'prioridad',
			'email',
			'edad',
			'sexo',
			'estado',
			'solicitud',
			'password',
		]

		labels={
			'nombre': 'Nombre',
			'apellido': 'Apellido',
			'direccion': 'Direccion,
			'telefono': 'Telefono',
			'celular'; 'Celular',
			'fecha_inscripcion': 'Fecha_inscripcion',
			'prioridad': 'Prioridad',
			'email': 'Email',
			'edad': 'Edad',
			'sexo': 'Sexo',
			'estado': 'Estado',
			'solicitud': 'Solicitud',
			'password': 'Password',

		}

		widgets={
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'apellido': forms.TextInput(attrs={'class':'form-control'}),
			'direccion': forms.TextInput(attrs={'class':'form-control'}),
			'telefono': forms.TextInput(attrs={'class':'form-control'}),
			'celular': forms.TextInput(attrs={'class':'form-control'}),
			'fecha_inscripcion': forms.TextInput(attrs={'class':'form-control'}),
			'prioridad':'2',
			'email': forms.TextInput(attrs={'class':'form-control'}),
			'edad': forms.TextInput(attrs={'class':'form-control'}),
			'sexo': forms.TextInput(attrs={'class':'form-control'}),
			'estado':'1',
			'solicitud':'1',
			'password':'nombre',
		}
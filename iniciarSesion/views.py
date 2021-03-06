from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

from modelsAdmin.models import Usuario, Administrador, Suscriptor

def iniciarSesion(request):
    error = (False, "")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        usuario = User.objects.filter(username=username.lower())
        if len(usuario) == 0:
            mensaje = "El usuario no fue encontrado"
            error = (True, mensaje)
        else:
            usuario = authenticate(username=username.lower(), password=password)
            if usuario is not None:
                user = Usuario.objects.filter(usuario=usuario)
                suscriptores = Suscriptor.objects.filter(usuario__usuario=usuario)
                administradores = Administrador.objects.filter(usuario__usuario=usuario)
                if len(suscriptores) != 0:
                    if suscriptores[0].estadoCuenta:
                        login(request, usuario)
                        return redirect('/suscriptor')
                    else:
                        error = (True, "Su cuenta no ha sido activada")
                elif len(administradores) != 0:
                    if administradores[0].estadoCuenta:
                        login(request, usuario)
                        return redirect('/administrador')
                    else:
                        error = (True, "Su cuenta no ha sido activada")
                else:
                    error = (True, "La cuenta no tiene un perfil asociado")
            else:
                mensaje = "Contraseña incorrecta"
                error = (True, mensaje)

    template = loader.get_template('iniciarSesion/index.html')
    ctx = {
        'error': error
    }
    return HttpResponse(template.render(ctx, request))

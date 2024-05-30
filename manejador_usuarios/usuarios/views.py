from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.http import HttpResponseRedirect
from .forms import UsuarioForm, EmpleadoForm
from django.urls import reverse
from django.contrib import messages


# Create your views here.

def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            crear_usuario(form)
            messages.add_message(request, messages.SUCCESS, 'El usuario fue creado exitosamente')
            return HttpResponseRedirect(reverse('crearUsuario'))
        else:
                print(form.errors)
    else:
        form = UsuarioForm()

    context = {
            'form': form,
        }
    return render(request, 'crearSolicitud.html', context)


def crear_empleado(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            crear_empleado(form)
            messages.add_message(request, messages.SUCCESS, 'El empleado fue creado exitosamente')
            return HttpResponseRedirect(reverse('crearEmpelado'))
        else:
                print(form.errors)
    else:
        form = UsuarioForm()

    context = {
            'form': form,
        }
    return render(request, 'crearSolicitud.html', context)
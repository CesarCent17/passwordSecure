from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import RegistroUsuario, RegistroContrasena
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Contrasena

# Create your views here.

@login_required
def home(request):
    usuario_actual = request.user
    listacontrasenas = usuario_actual.contrasena.all()
    form = RegistroContrasena()
    contexto = {'contrasenas': listacontrasenas, 'form':form}
    return render(request, 'gestor/home.html', contexto)

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuario(request.POST)
        if form.is_valid():
            form.save()
            usuario = form.cleaned_data['username']
            messages.success(request, f'Bienvenido {usuario}!')
            return redirect('home')
    else:
        form = RegistroUsuario()
    return render(request, 'gestor/registro.html', {'form':form})


@login_required
def nueva_passw(request):
    usuario_actual = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = RegistroContrasena(request.POST)
        if form.is_valid():
            passw = form.save(commit=False)
            passw.usuario = usuario_actual
            passw.save()
            return redirect('/')

    """else:
        form = RegistroContrasena()"""
    #return render(request, 'gestor/home.html', {'form':form})
    return redirect('/')

@login_required
def edicion_passw(request, id_contrasena):
    #obj_passw = Contrasena.objects.get(id=id_contrasena)
    obj_passw = get_object_or_404(Contrasena, pk=id_contrasena)
    return render(request, 'gestor/editar.html', {'obj_passw':obj_passw})

@login_required
def editar_passw(request, id_contrasena):
    obj_passw = get_object_or_404(Contrasena, pk=id_contrasena)
    if request.method == 'POST':
        passw_editada = request.POST['contrasena']
        obj_passw.passw = passw_editada
        obj_passw.save()
        messages.success(request, 'Contrasena actualizada exitosamente!')
        return redirect('/')

@login_required
def eliminar_passw(request, id_contrasena):
    obj_passw = get_object_or_404(Contrasena, pk=id_contrasena)
    obj_passw.delete()
    messages.success(request, 'Contrasena eliminada exitosamente!')
    return redirect('/')









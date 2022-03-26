from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistroUsuario
from django.contrib import messages

# Create your views here.

@login_required
def home(request):
    usuario_actual = request.user
    listacontrasenas = usuario_actual.contrasena.all()
    contexto = {'contrasenas': listacontrasenas}
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


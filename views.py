from django.shortcuts import render, redirect
import threading
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.decorators import login_required
from calculo.models import Usuario
from django.contrib import messages
from .forms import LimitCalculatorForm, DerivativeCalculatorForm
import matplotlib.pyplot as plt
import numpy as np
import io
import sympy
import base64
from django.contrib.auth import authenticate, login as django_login, logout as django_logout

def home(request):
    return render(request, 'home.html')

def derivatives(request):
    result_data = None
    if request.method == 'POST':
        form = DerivativeCalculatorForm(request.POST)
        if form.is_valid():
            function_expression = form.cleaned_data['function']
            try:
                f = sympy.sympify(function_expression)
                derivative = sympy.diff(f)
                result_data = str(derivative)
            except (ValueError, sympy.SympifyError):
                result_data = 'Función no válida'
    else:
        form = DerivativeCalculatorForm()
    return render(request, 'derivatives.html', {'form': form, 'result_data': result_data})

def factor(request):
    return render(request, 'factor.html')

def function(request):
    return render(request, 'function.html')

def graphics(request):
    x = np.linspace(-10, 10, 400)
    y = 3 / x
    # Crear el gráfico
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label='f(x) = 3/x', color='blue')
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Gráfico de f(x) = 3/x')
    plt.grid(True)
    plt.legend()
    # Convertir el gráfico en una imagen
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    grafico = base64.b64encode(buffer.read()).decode()
    plt.close()
    return render(request, 'graphics.html', {'grafico': grafico})

def calcular_f(x):
    return ((1/(x+1))-(1/4))/(x-3)

def limits(request):
    result_data = None
    if request.method == 'POST':
        form = LimitCalculatorForm(request.POST)
        if form.is_valid():
            x = form.cleaned_data['x_value']
            function_expression = form.cleaned_data['function']
            try:
                f = sympy.sympify(function_expression)
                fx = f.subs('x', x)
                result_data = [(x, fx)]
            except (ValueError, sympy.SympifyError):
                result_data = [('Error', 'Función no válida')]
    else:
        form = LimitCalculatorForm()
    return render(request, 'limits.html', {'form': form, 'result_data': result_data})

def radicals(request):
    return render(request, 'radicals.html')

def login(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')
        try:
            user = Usuario.objects.get(username=usuario)
            if user.password == password:
                django_login(request, user)
                return redirect('home')
            else:
                print('Contraseña incorrecta')
                messages.error(request, 'Usuario o contraseña incorrectos')
        except Usuario.DoesNotExist:
            print('Usuario no encontrado')
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'log.html')

@login_required
def logout(request):
    request.logout()
    return redirect('home')

def register(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')
        if usuario and password:
            if Usuario.objects.filter(username=usuario).exists():
                print('El nombre de usuario ya está en uso.')
                messages.error(request, 'El nombre de usuario ya está en uso.')
            else:
                nuevo_usuario = Usuario(username=usuario, password=password)
                nuevo_usuario.save()
                print('Usuario Registrado')
                messages.success(request, 'Usuario Registrado')
                return redirect('home')
        else:
            messages.error(request, 'Es necesario llenar todos los campos')
            print('Es necesario llenar todos los campos')
    return render(request, 'register.html')
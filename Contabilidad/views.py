from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# Create your views here.
@login_required(login_url='/signin/')
def index(request):
    return render(request,'index.html')


#view de catalogo de cuentas 
@login_required(login_url='/signin/')
def catalogoCuenta(request):
    return render(request,'catalogo_cuenta.html')

#view de Transacciones
@login_required(login_url='/signin/')
def transaccion(request):
    return render(request,'transaccion.html')

#view de Balance comprobacion
@login_required(login_url='/signin/')
def balanceComprobacion(request):
    return render(request,'balance_comprobacion.html')

#view de Estado de Resultados
@login_required(login_url='/signin/')
def estadoResultados(request):
    return render(request,'estado_resultados.html')

#view de Estado de capital
@login_required(login_url='/signin/')
def estadoCapital(request):
    return render(request,'estado_capital.html')

#view de Balance General
@login_required(login_url='/signin/')
def balanceGeneral(request):
    return render(request,'balance_general.html')

#view de signup
def signin(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm(),
                'error': 'Usuario o contraseña incorrectos'
            })
        else:
            login(request, user)
            return redirect('index')
    else:
        return render(request, 'signin.html', {'form': AuthenticationForm()})

@login_required(login_url='/signin/')
def signout(request):
    logout(request)
    return redirect('signin')
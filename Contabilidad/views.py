from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .models import Cuenta, Periodo, Transaccion

# Create your views here.
@login_required(login_url='/signin/')
def index(request):
    return render(request,'index.html')


#view de catalogo de cuentas 
@login_required(login_url='/signin/')
def catalogoCuenta(request):
    Cuentas = Cuenta.objects.all()
    
    return render(request,'catalogo_cuenta.html',{'Cuentas':Cuentas})


#view de Transacciones
@login_required(login_url='/signin/')
def transaccion(request):
    Transacciones = Transaccion.objects.all()
    return render(request,'transaccion.html',{
        'Transacciones':Transacciones}
                  )

#view de agregar transaccion
@login_required(login_url='/signin/')
def agregarTransaccion(request):
    Cuentas = Cuenta.objects.all().values('id','nombre')
    Periodos = Periodo.objects.all().values('id','nombre')
    context = {
        'Cuentas':Cuentas,
        'Periodos':Periodos
    }
    if request.method == 'POST':
        cuenta = request.POST['cuenta']
        periodo = request.POST['periodo']
        fecha = request.POST['fecha']
        descripcion = request.POST['descripcion']
        cuenta_debe = request.POST['debe']
        cuenta_haber = request.POST['haber']
        transaccion = Transaccion(cuenta_id=cuenta,periodo_id=periodo,fecha=fecha,descripcion=descripcion,debe=cuenta_debe,haber=cuenta_haber)
        transaccion.save()
        return redirect('transacciones')

    return render(request,'Transaccion/agregar_transaccion.html',
                context
                )

#view de eliminar transaccion
def eliminarTransaccion(request,id):
    transaccion = Transaccion.objects.get(id=id)
    transaccion.delete()
    return redirect('transacciones')

#view de agregar periodo
@login_required(login_url='/signin/')
def agregarPeriodo(request):
    if request.method == 'POST':
        nombre = request.POST['id_nombre']
        fecha_inicio = request.POST['fecha_inicio']
        fecha_fin = request.POST['fecha_final']
        
        perido = Periodo(nombre=nombre,fecha_inicio=fecha_inicio,fecha_fin=fecha_fin)
        perido.save()
        return redirect('transacciones')
    else:
        return render(request,'Transaccion/agregar_periodo.html')

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


def signout(request):
    logout(request)
    return redirect('signin')
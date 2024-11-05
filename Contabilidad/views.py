from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .models import Cuenta, Periodo, Transaccion
from django.db.models import Sum

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
    if request.method == 'POST':
        periodo = request.POST['periodo']
        transacciones = Transaccion.objects.filter(periodo_id=periodo)
        Periodos = Periodo.objects.all().values('id','nombre')
        context = { 
            'Transacciones':transacciones,
            'Periodos':Periodos
        }
        return render(request,'transaccion.html',context)
    else:
        Transacciones = Transaccion.objects.all()
        Periodos = Periodo.objects.all()
        contex = {
            'Transacciones':Transacciones,
            'Periodos':Periodos
        }
        return render(request,'transaccion.html',contex)

#view de agregar transaccion
@login_required(login_url='/signin/')
def agregarTransaccion(request):
    Cuentas = Cuenta.objects.all().values('id','nombre')
    Periodos = Periodo.objects.all().values('id','mes','ano')
    context = {
        'Cuentas':Cuentas,
        'Periodos':Periodos
    }
    if request.method == 'POST':
        cuentas = request.POST.getlist('cuenta')
        periodos = request.POST.getlist('periodo')
        fechas = request.POST.getlist('fecha')
        deudas = request.POST.getlist('debe')
        haberes = request.POST.getlist('haber')
        descripciones = request.POST.getlist('descripcion')

        for i in range(len(cuentas)):
            if cuentas[i] and periodos[i]:  # Asegúrate de que los campos necesarios estén completos
                transaccion = Transaccion(
                    cuenta_id=cuentas[i],
                    periodo_id=periodos[i],
                    fecha=fechas[i],
                    debe=deudas[i],
                    haber=haberes[i],
                    descripcion=descripciones[i]
                )
                transaccion.save()
        return redirect('transacciones')  # Redirigir a la vista de transacciones

    else:
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
        mes = request.POST.get('mes')  # Cambia a get para evitar MultiValueDictKeyError
        ano = request.POST.get('ano')
        
        if mes and ano:  # Verifica que mes y ano no sean None
            periodo = Periodo(mes=int(mes), ano=int(ano))  # Convierte a entero si es necesario
            periodo.save()
            return redirect('transacciones')  # Asegúrate de que 'transacciones' sea el nombre correcto
    else:
        meses = range(1, 13)  # Crear una lista de meses
        
    return render(request, 'Transaccion/agregar_periodo.html', {'meses': meses})

#view de totalizar periodo
@login_required(login_url='/signin/')
def totalizar(request):
    # Calcula el total de 'debe' y 'haber'
    total_debe = Transaccion.objects.aggregate(total_debe=Sum('debe'))['total_debe'] or 0
    total_haber = Transaccion.objects.aggregate(total_haber=Sum('haber'))['total_haber'] or 0
    
    # Obtiene todas las transacciones para mostrarlas en la vista
    transacciones = Transaccion.objects.all()
    
    return render(request, 'Transaccion/totalizar.html', {
        'total_debe': total_debe,
        'total_haber': total_haber,
        'transacciones': transacciones,
    }) 

#libro mayor
def libroMayor(request):
    # Agrupar las transacciones por cuenta y calcular totales
    cuentas_con_totales = (
        Transaccion.objects.values('cuenta__id', 'cuenta__nombre')
        .annotate(total_debe=Sum('debe'), total_haber=Sum('haber'))
        .order_by('cuenta__id')
    )
    
    # Obtener todas las transacciones ordenadas por cuenta
    transacciones = Transaccion.objects.order_by('cuenta__id', 'fecha')
    
    return render(request, 'Transaccion/libro_mayor.html', {
        'cuentas_con_totales': cuentas_con_totales,
        'transacciones': transacciones,
    })





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
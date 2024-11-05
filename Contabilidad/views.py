from django.db.models import Sum
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .models import Cuenta, Periodo, Transaccion
from django.db.models import Sum, F


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
        Periodos = Periodo.objects.all().values('id','mes','ano')
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
        # Calcula el total de 'debe' y 'haber'
    total_debe = Transaccion.objects.aggregate(total_debe=Sum('debe'))['total_debe'] or 0
    total_haber = Transaccion.objects.aggregate(total_haber=Sum('haber'))['total_haber'] or 0
    
    # Obtiene todas las transacciones para mostrarlas en la vista
    transacciones = Transaccion.objects.all()
    
    return render(request, 'balance_comprobacion.html', {
        'total_debe': total_debe,
        'total_haber': total_haber,
        'transacciones': transacciones,
    }) 

#view de Estado de Resultados
@login_required(login_url='/signin/')
def estadoResultados(request):
    
    ingresos = Cuenta.objects.filter(tipo='INGRESOS')
    costos_venta = Cuenta.objects.filter(tipo='COSTOS_DE_VENTA')  # Asegúrate de que el tipo exista
    gastos = Cuenta.objects.filter(tipo='GASTOS')  # Esto incluye todos los gastos

    # Calcular ingresos totales
    total_ingresos = sum(
        transaccion.haber
        for cuenta in ingresos
        for transaccion in Transaccion.objects.filter(cuenta=cuenta)
    )

    # Calcular costos de ventas totales
    total_costos_venta = sum(
        transaccion.debe
        for cuenta in costos_venta
        for transaccion in Transaccion.objects.filter(cuenta=cuenta)
    )

    # Calcular gastos operativos totales
    total_gastos = sum(
        transaccion.debe
        for cuenta in gastos
        for transaccion in Transaccion.objects.filter(cuenta=cuenta)
    )

    # Cálculos del estado de resultados
    utilidad_bruta = total_ingresos - total_costos_venta
    utilidad_operativa = utilidad_bruta - total_gastos

    # Otros ingresos y gastos
    otros_ingresos = Transaccion.objects.filter(cuenta__tipo='RESULTADO_ACREEDOR').aggregate(total=Sum(F('haber')))['total'] or 0
    otros_gastos = Transaccion.objects.filter(cuenta__tipo='RESULTADO_DEUDOR').aggregate(total=Sum(F('debe')))['total'] or 0

    # Utilidad Antes de Impuestos
    utilidad_antes_impuestos = utilidad_operativa + otros_ingresos - otros_gastos

    # Impuestos sobre la renta (suponiendo un 30%)
    impuestos = utilidad_antes_impuestos * 0.30 if utilidad_antes_impuestos > 0 else 0

    # Utilidad Neta
    utilidad_neta = utilidad_antes_impuestos - impuestos

    return render(request, 'estado_resultados.html', {
    'total_ingresos': total_ingresos,
    'total_costos_venta': total_costos_venta,
    'total_gastos': total_gastos,
    'utilidad_bruta': utilidad_bruta,
    'utilidad_operativa': utilidad_operativa,
    'otros_ingresos': otros_ingresos,
    'otros_gastos': otros_gastos,
    'utilidad_antes_impuestos': utilidad_antes_impuestos,
    'impuestos': impuestos,
    'utilidad_neta': utilidad_neta,
})

#view de Estado de capital
@login_required(login_url='/signin/')
def estadoCapital(request):
        # Filtra las cuentas que inician con "3" y obtiene sus transacciones
    transacciones_capital = Transaccion.objects.filter(cuenta__codigo__startswith="3")
    
    # Calcula el saldo para cada cuenta
    saldos_capital = {}
    for transaccion in transacciones_capital:
        cuenta_nombre = transaccion.cuenta.nombre
        saldo = saldos_capital.get(cuenta_nombre, 0) + (transaccion.debe - transaccion.haber)
        saldos_capital[cuenta_nombre] = saldo
    
    # Calcula el total de capital
    total_capital = sum(saldos_capital.values())
    
    return render(request, 'estado_capital.html', {
        'saldos_capital': saldos_capital,
        'total_capital': total_capital,
    })

#view de Balance General
@login_required(login_url='/signin/')
def balanceGeneral(request):
    # Obtener todas las cuentas de cada tipo
    activos = Cuenta.objects.filter(tipo='ACTIVO')
    pasivos = Cuenta.objects.filter(tipo='PASIVO')
    patrimonio = Cuenta.objects.filter(tipo='PATRIMONIO')

    # Calcular total de activos
    total_activos = sum(
        transaccion.debe - transaccion.haber
        for cuenta in activos
        for transaccion in Transaccion.objects.filter(cuenta=cuenta)
    )

    # Calcular total de pasivos
    total_pasivos = sum(
        transaccion.debe - transaccion.haber
        for cuenta in pasivos
        for transaccion in Transaccion.objects.filter(cuenta=cuenta)
    )

    # Calcular total de patrimonio
    total_patrimonio = sum(
        transaccion.debe - transaccion.haber
        for cuenta in patrimonio
        for transaccion in Transaccion.objects.filter(cuenta=cuenta)
    )

    # Crear un diccionario con los resultados
    context = {
        'total_activos': total_activos,
        'total_pasivos': total_pasivos,
        'total_patrimonio': total_patrimonio,
        'saldo_total': total_activos - (total_pasivos + total_patrimonio)  # Para verificar la ecuación
    }

    return render(request, 'balance_general.html', context)




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
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')


#view de catalogo de cuentas 
def catalogoCuenta(request):
    return render(request,'catalogo_cuenta.html')

#view de Transacciones
def transaccion(request):
    return render(request,'transaccion.html')

#view de Balance comprobacion
def balanceComprobacion(request):
    return render(request,'balance_comprobacion.html')

#view de Estado de Resultados
def estadoResultados(request):
    return render(request,'estado_resultados.html')

#view de Estado de capital
def estadoCapital(request):
    return render(request,'estado_capital.html')

#view de Balance General
def balanceGeneral(request):
    return render(request,'balance_general.html')
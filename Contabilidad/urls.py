from django.urls import path
from . import views


urlpatterns = [
    path('', views.signin, name='signin'),
    path('signin/', views.signin),
    path('index', views.index, name='index'),
    path('catalogoCuenta/', views.catalogoCuenta, name='catalogoCuenta'),
    
    #transacciones
    path('transacciones/', views.transaccion, name='transacciones'),
    path('transacciones/agregarTransaccion/', views.agregarTransaccion, name='agregarTransaccion'),
    path('transacciones/eliminarTransaccion/<id>', views.eliminarTransaccion, name='eliminarTransaccion'),
    path('transacciones/agregarPeriodo/', views.agregarPeriodo, name='agregarPeriodo'),
    
    #Totalizar
    path('transacciones/totalizar/', views.totalizar, name='totalizar'),
    
    #libro mayor
    path('transacciones/verLibroMayor/', views.libroMayor, name='libro'),
    
    #balance de comprobacion
    path('balanceComprobacion/', views.balanceComprobacion,name='balanceComprobacion'),
    
    
    path('estadoResultados/', views.estadoResultados, name='estadoResultados'),
    
    #estado de capital
    path('estadoCapital/', views.estadoCapital, name='estadoCapital'),
    
    #balance general
    path('balanceGeneral/', views.balanceGeneral, name='balanceGeneral'),
    
    path('signout/', views.signout, name='signout'),
    
]

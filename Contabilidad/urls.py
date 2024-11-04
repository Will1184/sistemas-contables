from django.urls import path
from . import views


urlpatterns = [
    path('', views.signin, name='signin'),
    path('signin/', views.signin),
    path('index', views.index, name='index'),
    path('catalogoCuenta/', views.catalogoCuenta, name='catalogoCuenta'),
    path('transacciones/', views.transaccion, name='transacciones'),
    path('transacciones/agregarTransaccion/', views.agregarTransaccion, name='agregarTransaccion'),
    path('transacciones/agregarPeriodo/', views.agregarPeriodo, name='agregarPeriodo'),
    path('balanceComprobacion/', views.balanceComprobacion,name='balanceComprobacion'),
    path('estadoResultados/', views.estadoResultados, name='estadoResultados'),
    path('estadoCapital/', views.estadoCapital, name='estadoCapital'),
    path('balanceGeneral/', views.balanceGeneral, name='balanceGeneral'),
    path('signout/', views.signout, name='signout'),
    
]

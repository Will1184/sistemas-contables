from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('catalogoCuenta/', views.catalogoCuenta),
    path('transacciones/', views.transaccion),
    path('balanceComprobacion/', views.balanceComprobacion),
    path('estadoResultados/', views.estadoResultados),
    path('estadoCapital/', views.estadoCapital),
    path('balanceGeneral/', views.balanceGeneral),
]

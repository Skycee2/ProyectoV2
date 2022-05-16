from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('carrito/', carrito, name="carrito"),
    path('registro/', registro, name="registro"),
    path('seguimiento/', seguimiento, name="seguimiento"),
    path('subscribirse/', subscribirse, name="subscribirse"),
    path('cuenta/', cuenta, name="cuenta"),
    path('agregar_productos/', agregar_productos, name="agregar_producto"),
    path('modificar_productos/<codigo>/', modificar_producto, name="modificar_producto"),
    path('eliminar_producto/<codigo>/', eliminar_producto, name="eliminar_producto"),
    path('listar_productos/', listar_productos, name="listar_productos"),
    path('agregar_usuarios/', agregar_usuarios, name="agregar_usuarios"),
    path('modificar_usuarios/<id_usuario>/', modificar_usuarios, name="modificar_usuarios"),
    path('historialpedidos/', historialpedidos, name="historialpedidos"),
    path('eliminar/<id_usuario>/', eliminar_Usuarios, name="eliminar_usuarios"),
    path('listar_usuarios/', listar_usuarios, name="listar_usuarios"),
    path('home_usuario/', home_usuario, name="home_usuario"),
    path('exitosamente/', exitosamente, name="exitosamente"),
]

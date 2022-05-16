from pyexpat import model
from django.db import models
from tkinter import Widget
from django import forms

# modelos productos
class CategoriaProducto(models.Model):
    categoria = models.CharField(max_length=30)

    def __str__(self):
        return self.categoria
    
    class Meta:
        db_table = 'db_categoria_producto'

class Producto(models.Model):
    codigo = models.AutoField(null=False,primary_key=True)
    nombre = models.CharField(max_length=50)
    marca =  models.CharField(max_length=50)
    stock = models.IntegerField()
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    stock = models.IntegerField()
    categoria = models.ManyToManyField(CategoriaProducto, related_name='categorias')
    imagen = models.ImageField(upload_to="productos", null=True) 
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre
    
    def get_categorias(self):
        return "\n".join([c.categoria for c in self.categoria.all()])
    
    class Meta:
        db_table = 'db_producto'



#usuario

class TipoUsuario(models.Model):
    tipo_usuario = models.CharField(max_length=20)

    def __str__(self):
        return self.tipo_usuario

    class Meta:
        db_table = "db_tipo_usuario"

class EstadoSub(models.Model):
    estado_sub = models.CharField(max_length=20)

    def __str__(self):
        return self.estado_sub

    class Meta:
        db_table = "db_estado_sub"

class Usuario(models.Model):
    id_usuario = models.IntegerField(null=False, primary_key=True)
    nombre_usuario = models.CharField(max_length=20)
    pass_usuario = models.CharField(max_length=20)
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    telefono_usuario = models.IntegerField(editable=True)
    correo_usuario = models.EmailField(max_length=30)
    imagen_usuario = models.ImageField(upload_to="usuarios", null=True) 
    direccion_usuario = models.CharField(max_length=40)
    estado_sub = models.ForeignKey(EstadoSub, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)



class itemsCarrito(models.Model):
    nombre_producto = models.CharField(max_length=40)
    precio_producto = models.IntegerField()
    imagen = models.ImageField(upload_to="itemsCarrito",null=True)
    marca = models.CharField(max_length=40)
    stock = models.IntegerField()
    
    def __str__(self):
        return self.nombre_producto
    
    class Meta:
        db_table = 'db_itemsCarrito'


#python manage.py makemigrations
#python manage.py migrate
#python manage.py createsuperuser
#python manage.py runserver


        
from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

# vistas producto
#agregar productos
def agregar_productos (request):
    datos = {
        'form' : ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Producto agregado correctamente!'
    return render (request, 'app/agregar_productos.html', datos)


#agregar usuario
def agregar_usuarios (request):
    datos = {
        'form' : UsuarioForm()
    }
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Usuario agregado correctamente'
    return render (request, 'app/agregar_usuarios.html', datos)

#modificar producto
def modificar_producto (request, codigo):
    varibleTemporal = Producto.objects.get(codigo=codigo)
    datos = {
        'form' : ProductoForm(instance=varibleTemporal)
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES, instance=varibleTemporal)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Producto modificado correctamente'
            datos['form'] = formulario
    return render (request, 'app/modificar_productos.html', datos)



#modificar usuarios
def modificar_usuarios (request, id_usuario):
    varibleTemporal = Usuario.objects.get(id_usuario=id_usuario)
    datos = {
        'form' : UsuarioForm(instance=varibleTemporal)
    }
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST, files=request.FILES, instance=varibleTemporal)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Usuario modificado correctamente'
            datos['form'] = formulario
    return render (request, 'app/modificar_usuarios.html', datos)


#eliminar producto
def eliminar_producto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()

    return redirect(to="listar_productos")


#listar productos
def listar_productos(request):
        productoAll = Producto.objects.all()
        
        datos = {
            'listarProductos' : productoAll
        }
        return render(request, 'app/listar_productos.html',datos)



# SECCION ELIMINAR
#eliminar usuarios
def eliminar_Usuarios(request, id_usuario):
    usuario = Usuario.objects.get(id_usuario=id_usuario)
    usuario.delete()

    return redirect(to="listar_usuarios")

#eliminar producto
def eliminar_producto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()

    return redirect(to="listar_productos")


#listar usuarios
def listar_usuarios (request):
    usuarioAll = Usuario.objects.all()
    datos = {
        'listarUsuarios' : usuarioAll
    }
    return render (request, 'app/listar_usuarios.html', datos)


# vista listar todos
#enviar carrito en data
def index(request):
    productoAll = Producto.objects.all()
    datos = {
        'listaProductos' : productoAll
    }
        
    return render(request, 'app/index.html', datos)

# vistas paginas
def listar (request):
    return render (request, 'app/listar_productos.html')



def carrito(request):
    carrito = itemsCarrito.objects.all()
    datos = {
        'listarCarrito' : carrito
    }
    return render(request, 'app/carrito.html',  datos  )





def registro(request):
    return render(request, 'app/registro.html')

def seguimiento(request):
    return render(request, 'app/seguimiento.html')

def subscribirse(request):
    return render(request, 'app/subscribirse.html') 

def historialpedidos(request):
    return render(request, 'app/historialpedidos.html') 


def cuenta(request):
    return render(request, 'app/cuenta.html') 

def agregar_producto(request):
    return render(request, 'app/agregar.html')



def home_usuario(request):
    productoAll = Producto.objects.all()
    datos = {
        'listaProductos' : productoAll
    }
    if request.method == 'POST':
        carrito = itemsCarrito()
        carrito.nombre_producto = request.POST.get('nombre_producto')
        carrito.precio_producto = request.POST.get('precio_producto')
        carrito.imagen = request.POST.get('imagen')
        carrito.marca = request.POST.get('marca')
        carrito.stock = request.POST.get('stock')
        carrito.save()
        
    return render(request, 'app/home_usuario.html', datos)


def exitosamente(request):
    carrito = itemsCarrito.objects.all()   
    carrito.delete()

    return render(request, 'app/exitosamente.html')






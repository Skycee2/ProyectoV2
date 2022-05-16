from django.contrib import admin
from .models import *
from django.forms import CheckboxSelectMultiple

# Register your models here.



#producto
class ProductosAdmin(admin.ModelAdmin):
    list_display = ['codigo','nombre','marca','precio','descripcion','stock','get_categorias','imagen','create_at','update_at']
    search_fields = ['codigo']
    list_per_pages = 5

#usuario
class UsuariosAdmin(admin.ModelAdmin):
    list_display = ['id_usuario','nombre_usuario','pass_usuario','tipo_usuario','telefono_usuario', 'correo_usuario','imagen_usuario','direccion_usuario','estado_sub']
    search_fields = ['ID']
    list_per_page = 5

class CarritoAdmin(admin.ModelAdmin):
    list_display = ['nombre_producto','precio_producto','imagen','marca','stock']
    list_per_pages = 5

#producto
admin.site.register(CategoriaProducto)
admin.site.register(Producto, ProductosAdmin)
#usuario
admin.site.register(TipoUsuario)
admin.site.register(EstadoSub)
admin.site.register(Usuario, UsuariosAdmin)

admin.site.register(itemsCarrito, CarritoAdmin)
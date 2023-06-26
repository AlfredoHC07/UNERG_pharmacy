from django.contrib import admin
from .models import CustomUser,Producto,Almacen
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Producto)
admin.site.register(Almacen)
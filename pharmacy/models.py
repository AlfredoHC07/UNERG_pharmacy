from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    telefono = models.CharField(max_length=11)
    direccion = models.CharField(max_length=350)
    correo = models.CharField(max_length=150) 
    contraseña = models.CharField(max_length=100) 
    is_admin = models.BooleanField(default=False)
    is_almacen = models.BooleanField(default=False)

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=255)
    precio_compra = models.DecimalField(max_digits=20,decimal_places=2)
    precio_venta = models.DecimalField(max_digits=12,decimal_places=2)
    disponibilidad = models.BooleanField(default=False)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='imagenes/', blank=True, null=True)

class Almacen(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha_entrada = models.DateTimeField(auto_now_add=True)
    cantidad_producto = models.IntegerField()
    cantidad_producto_vendidos = models.IntegerField()

class TablaVentas(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_producto_actual = models.IntegerField()
    precio_total_compra = models.DecimalField(max_digits=20,decimal_places=2)
    precio_total_venta = models.DecimalField(max_digits=20,decimal_places=2)
    ganancias =models.DecimalField(max_digits=500,decimal_places=2)
    reportes = models.TextField()
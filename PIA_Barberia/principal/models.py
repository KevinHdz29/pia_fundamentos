from django.db import models

# Create your models here.
 
class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField() 
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    duracion = models.PositiveIntegerField() 
    disponible = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
    
##########################################################################################

class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)  
    horario = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre 
    
    
##########################################################################################
# Investigamos como usar las foreignkey
# ForeignKey requiere al menos dos argumentos: el modelo relacionado y on_delete
# Usar PROTECT garantiza la integridad de estos datos en Django ( en lugar de cascade)

class Estilista(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    descripcion = models.TextField()
    sucursal = models.ForeignKey(
        Sucursal,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.nombre
    
##########################################################################################

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    existencia = models.PositiveIntegerField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

##########################################################################################

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre + " " + self.apellido

##########################################################################################

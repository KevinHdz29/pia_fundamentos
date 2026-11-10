from django.contrib import admin
from .models import Servicio, Sucursal, Estilista, Producto, Cliente

admin.site.register(Servicio)
admin.site.register(Sucursal)
admin.site.register(Estilista)
admin.site.register(Producto)
admin.site.register(Cliente)
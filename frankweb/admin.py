from django.contrib import admin
from .models import Empleados,Area,Servicio,Cliente,Producto,Produccion,Visitas,Asistencia
# Register your models here.
admin.site.register(Empleados)
admin.site.register(Area)
admin.site.register(Servicio)
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Produccion)
admin.site.register(Visitas)
admin.site.register(Asistencia)

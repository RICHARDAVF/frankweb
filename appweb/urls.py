"""appweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from frankweb import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="index"),
    path('administrador/', views.administrador,name="administrador"),
    path('search_person/',views.search_person, name='search_person'),
    path('guardar_firma/',views.guardar_firma, name='guardar_firma'),
    path('registro_salida/',views.RegistroScontroler, name='registro_salida'),
    path('login/', views.loginUser,name="login"),
    path('logout/', views.logoutUser,name="logout"),
    path('registro/', views.registro,name="registro"),
    path('controler/', views.controler,name="controler"),
    path('vigilancia/', views.vigilancia,name="vigilancia"),
    path('registrar_visita/', views.registrar_visita,name="registrar_visita"),
    path('empleados/', views.empleados,name="empleados"),
    path('asistencias/', views.asistencias,name="asistencias"),
    path('formatear/', views.formatear,name="formatear"),
    path('produccion/', views.produccion,name="produccion"),
    path('servicio/', views.mas,name="servicio"),
    
]

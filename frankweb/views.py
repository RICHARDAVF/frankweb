from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Empleados,Visitas
from .forms import*
from django.db import IntegrityError
import base64
from io import BytesIO
from PIL import Image
from django.utils import timezone
from django.contrib.auth.decorators import login_required



# Create your views here.

def index(request):
     return render(request, 'index.html')
@login_required
def administrador(request):
     return render(request, "administrador.html")
@login_required
def asistencias(request):
     datos = Asistencia.objects.all()
     return render(request, "asistencias.html",{"datos":datos})
@login_required
def produccion(request):
     datos = Produccion.objects.all()
     return render(request, "produccion.html", {"datos":datos})
@login_required
def mas(request):
     servicios = Servicio.objects.all()
     clientes = Cliente.objects.all()
     productos = Producto.objects.all()
     return render(request, "servicios.html", {"servicios":servicios,"clientes":clientes,"productos":productos})
def formatear(request):
     Asistencia.objects.all().update(
          fecha=date(2023,1,1),
          hora_entrada=time(0,0,0),
          hora_salida=time(0,0,0),
          estado=0,
          observacion = "ninguna"
     )
     datos = Asistencia.objects.all()
     return render(request, "asistencias.html", {"datos":datos})
def loginUser(request):

     if request.method == 'POST':
          user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
          if user is not None:
               login(request,user)
               return  redirect("registro")
          else:
               return render(request, 'login.html',{"form":LoginForm,"error":"Usuario o contraseña incorrecto"})
     return render(request, 'login.html',{'form':LoginForm})
def logoutUser(request):
     logout(request)
     return redirect('index')
@login_required
def registro(request):
     if request.method == 'POST':
          if request.POST["password1"] == request.POST["password2"]:
               try:
                    user = User.objects.create_user(username=request.POST["username"],email=request.POST["email"], password=request.POST["password2"])
                    user.save()
                    login(request,user)
                    return redirect('index')
               except IntegrityError:
                    return render(request,"registro.html",{"form",RegistroForm,"Error","El usuario ya existe"})
          else:
               return render(request, "registro.html", {"form": RegistroForm, "error": "Las contraseñas no coinciden"})


     return render(request, 'registro.html',{"form":RegistroForm})
def empleados(request):
     if request.method =="POST":
         pass
     return render(request, 'empleados.html',{"form":EmpleadosForm})
def search_person(request):
    query = request.GET.get('q')
    results = Empleados.objects.filter(dni=query)

    data = [{'dni': "", 'nombre':"", 'apellidos':""}]
    if len(list(results))>0:
          data = [{'dni': p.dni, 'nombre': p.nombre, 'apellidos': p.apellidos,} for p in results]
          
    return JsonResponse({'data': data})
@login_required
def controler(request):
     if request.method == "POST":
          area = Area.objects.get(id=request.POST["area"])
          servicio = Servicio.objects.get(id=request.POST["servicio"])
          cliente = Cliente.objects.get(id=request.POST["cliente"])
          producto = Producto.objects.get(id=request.POST["producto"])
          form = Produccion(dni=request.POST["dni"],nombre=request.POST["nombre"],apellido=request.POST["apellido"],\
                            hora_inicio=request.POST["hora_inicio"],fecha=request.POST["fecha"],area=area,servicio=servicio,cliente=cliente,producto=producto,validacion=1)
          form.save()
     return render(request,'controler.html',{"form":RegistroControlerForm})
@login_required
def RegistroScontroler(request):
     if request.method == "POST":
          dni = request.POST["dni"]
          try:
               produccion = Produccion.objects.get(dni=dni,validacion=2)
               produccion.orden_servicio = request.POST["orden_servicio"]
               produccion.orden_produccion = request.POST["orden_produccion"]
               produccion.lote = request.POST["lote"]
               produccion.kilos = request.POST["kilos"]
               produccion.turno = request.POST["turno"]
               produccion.hora_salida = request.POST["hora_salida"]
               produccion.save()
          except :
               pass
     return render(request,'controler.html',{"form":RegistroControlerForm})
@login_required
def vigilancia(request):
     if request.method == "POST":
          try:
               empleado = Asistencia.objects.get(dni=request.POST['dni'],estado=0)
               empleado.hora_entrada = timezone.localtime().time()
               empleado.fecha=timezone.localdate()
               empleado.observacion=request.POST["observacion"]
               empleado.estado = empleado.estado + 1
               empleado.save()
          except:
               empleado = Asistencia.objects.get(dni=request.POST['dni'],estado=1)
               empleado.hora_salida = timezone.localtime().time()
               empleado.observacion=empleado.observacion+"/"+request.POST["observacion"]
               empleado.estado = empleado.estado + 1
               empleado.save()
          
     return render(request,"vigilancia.html",{"form1":VigilanciaForm,"form2":VisitaForm})
@login_required
def registrar_visita(request):
     if request.method == "POST":

          form = Visitas(dni=request.POST["dni"],nombre=request.POST["nombre"],apellidos=request.POST["apellidos"])
          form.save()
          return redirect('vigilancia')


def guardar_firma(request):
     if request.method == 'POST':
          image_b64 = request.POST.get('image_b64')
          dni = request.POST.get('dni')
          # Obtener el objeto del modelo por ID o cualquier otro criterio de búsqueda
          objeto_modelo = Produccion.objects.get(dni=dni,validacion=1)

          # Decodificar la imagen y guardarla en un archivo BytesIO
          image = Image.open(BytesIO(base64.b64decode(image_b64)))
          foto_buffer = BytesIO()
          image.save(foto_buffer, format='PNG')
          
          # Actualizar el campo "foto" del objeto del modelo con los datos de imagen recién escritos
          objeto_modelo.firma.save(f"{dni}{datetime.now().strftime('%H:%M:%S')}.png", foto_buffer, save=True)
          objeto_modelo.validacion=2
          # Guardar el objeto del modelo actualizado en la base de datos
          objeto_modelo.save()

          response = JsonResponse({'success': True})
          return response
     else:
          response = JsonResponse({'success': False})
          return response
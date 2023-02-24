from django import forms
from .models import*
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Nombre de usuario'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder':'Contraseña'}))
        

       
class RegistroForm(AuthenticationForm):
    
    username = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Nombre de usuario'}))
    email = forms.EmailField(widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Correo Electronico'}))
    password1 = forms.CharField(widget = forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder':'Contraseña'}))
    password2 = forms.CharField(widget = forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder':'Repita la Contraseña'}))

class RegistroControlerForm(forms.ModelForm):
    class Meta:
        model = Produccion
        fields ='__all__'
        widgets ={
            "dni":forms.TextInput(attrs={"class": 'form-control', 'placeholder':"Documento","id":"dni","name":"dni"}),
            "nombre":forms.TextInput(attrs={"class": 'form-control', 'placeholder':"Nombre","id":"nombre","name":"nombre"}),
            "apellido":forms.TextInput(attrs={"class": 'form-control', 'placeholder':"Apellido","id":"apellidos","name":"apellidos"}),
            "hora_inicio":forms.TimeInput(attrs={"class": 'form-control',"id":"hora_inicio","name":"hora_inicio" ,"type":"time"}),
            "hora_salida":forms.TimeInput(attrs={"class": 'form-control',"id":"hora_salida","name":"hora_salida" ,"type":"time"}),
            "fecha":forms.DateInput(attrs={"class": 'form-control',"id":"fecha","name":"fecha" ,"type":"date"}),
            "area":forms.Select(attrs={"class": 'form-control',"id":"area","name":"area" ,"type":"select"}),
            "servicio":forms.Select(attrs={"class":"form-control","id":"servicio","name":"servicio" ,"type":"select"}),
            "cliente":forms.Select(attrs={"class":"form-control","id":"cliente","name":"cliente" ,"type":"select"}),
            "producto":forms.Select(attrs={"class":"form-control","id":"producto","name":"producto" ,"type":"select"}),
            "turno":forms.Select(attrs={"class":"form-control","id":"turno","name":"turno" ,"type":"select"}),
            "orden_produccion":forms.TextInput(attrs={"class":"form-control","id":"orden_produccion","name":"orden_produccion" }),
            "orden_servicio":forms.TextInput(attrs={"class":"form-control","id":"orden_servicio","name":"orden_servicio"}),
            "lote":forms.TextInput(attrs={"class":"form-control","id":"lote","name":"lote"}),
            "kilos":forms.NumberInput(attrs={"class":"form-control","id":"kilos","name":"kilos" ,"type":"number"}),
        }
  
class VigilanciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = "__all__"
        widgets = {
            "dni" :forms.TextInput(attrs = {"class": "form-control","placeholder":"Documento","id":"dni","name":"dni"}),
            "nombre":forms.TextInput(attrs = {"class": "form-control","placeholder":"Nombre","id": "nombre","name": "nombre"}),
            "apellidos":forms.TextInput(attrs = {"class": "form-control","placeholder":"Apellidos","id":"apellidos","name":"apellidos"}),
            "turno":forms.Select(attrs = {"class": "form-select","id":"turno","name":"turno"}),
            "area":forms.Select(attrs = {"class":"form-select","id":"area","name":"area"}),
            "observacion":forms.TextInput(attrs ={"class":"form-control","name":"observacion","id":"observacion"})

        }

    
class VisitaForm(forms.ModelForm):
    class Meta:
        model = Visitas
        fields ="__all__"
        widgets = {
            "dni":forms.TextInput(attrs={"class":"form-control","name":"dni","id":"dni","placeholder":"Documento"}),
            "nombre":forms.TextInput(attrs={"class":"form-control","name":"nombre","id":"nombre","placeholder":"Ingrese su nombre"}),
            "apellidos":forms.TextInput(attrs={"class":"form-control","name":"apellidos","id":"apellidos","placeholder":"Ingrese su apellido"})
        }
class EmpleadosForm(forms.ModelForm):
    class Meta:
        model = Empleados
        fields =["dni","nombre","apellidos"]
        widgets ={
            "dni":forms.TextInput(attrs={"class":"form-control","name":"dni","id":"dni","placeholder":"Documento"}),
            "nombre":forms.TextInput(attrs={"class":"form-control","name":"nombre","id":"nombre","placeholder":"Ingrese su nombre"}),
            "apellidos":forms.TextInput(attrs={"class":"form-control","name":"apellidos","id":"apellidos","placeholder":"Ingrese su apellido"})
        
        }
   
    
    
    
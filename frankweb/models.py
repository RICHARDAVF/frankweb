from django.db import models

from datetime import time,datetime,date
# Create your models here.
ESTADO =[("S","SOLTERO(A)"),("C","CASADO(A)"),("D","DIVORCIADO(A)"),("CO","CONVIVIENTE")]
SEXO = [("F","FEMENINO"),("M","MASCULINO")]
AREA = [("EMP","EMPLEADO"),("ADM","ADMINISTRADOR"),("MNT","MANTENIMIENTO")]

PENSION =[("ONP","ONP"),("AFP HABITAT","AFP HABITAT"),("AFP INTEGRA","AFP INTEGRA"),("AFP PRIMA","AFP PRIMA"),\
          ("AFP PROFUTURO","AFP PROFUTURO")]
EDUCACION =[("PRIMARIA","PRIMARIA"),("SECUNDARIA","SECUNDARIA",),("TECNICO","TECNICO"),("UNIVERSITARIO","UNIVERSITARIO"),\
            ("MAESTRIA","MAESTRIA"),("TITULADO","TITULADO")]
class Empleados(models.Model):
   
    nombre = models.CharField(max_length=25,verbose_name="Nombres",null=True)
    apellidos = models.CharField(max_length=25,verbose_name="Apellidos",null=True)
    dni = models.CharField(max_length=12,verbose_name="Documento",unique=True)
    email = models.EmailField(max_length=50,verbose_name="Email",unique=True)
    telefono = models.CharField(max_length=15,verbose_name="Telefono",null=True)
    sexo = models.CharField(max_length=2, choices=SEXO,verbose_name="Sexo",null=True)
    estado_civil = models.CharField(max_length=2,choices=ESTADO,verbose_name="Estado Civil",null=True)
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento",null=True)
    foto = models.ImageField(upload_to="fotoempleados/",verbose_name="Foto",null=True)
    direccion = models.CharField(max_length=100,verbose_name="Direccion",null=True)
    ingles = models.BooleanField(default=False,verbose_name="Ingles",null=True)
    area = models.CharField(max_length=5,choices=AREA,verbose_name="Area",null=True)
    codigo_contable = models.CharField(max_length=25,verbose_name="Codigo Contable",null=True)
    inicio_contrato= models.DateField(verbose_name="Inicio de Contrato",null=True)
    fin_contrato = models.DateField(verbose_name="Fin de Contrato",null=True)
    
    salario = models.DecimalField(default=0.00,max_digits=9,decimal_places=2,verbose_name="Salario",null=True)
    jornal = models.DecimalField(default=0.00,max_digits=9,decimal_places=2,verbose_name="Jornal",null=True)
    bono = models.DecimalField(default=0.00,max_digits=9,decimal_places=2,verbose_name="Bono",null=True)
    movilidad = models.BooleanField(default=False,verbose_name="Movilidad",null=True)
    carne_essalud = models.CharField(max_length=50,verbose_name="Carne ESSLAUD",null=True)
    carne_cupss = models.CharField(max_length=50,verbose_name="Carne CUPPS",null=True)
    cuenta_haberes = models.CharField(max_length=15,verbose_name="Cuenta Haberes",null=True)
    asignacion_familiar = models.BooleanField(default=False,verbose_name="Asignacion Familiar",null=True)
    hora_entrada = models.TimeField(verbose_name="Hora de Entrada",null=True)
    pension = models.CharField(max_length=20,verbose_name="Pension",choices=PENSION,null=True)
    educacion = models.CharField(max_length=20,choices=EDUCACION,verbose_name="Educacion",null=True)

    
    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        db_table = "empleados"
        ordering = ["id"]
    def __str__(self) -> str:
        return self.nombre
class Area(models.Model):
    area = models.CharField(max_length=150,verbose_name="Area")
    def __str__(self) -> str:
        return self.area
    class Meta:
        verbose_name = "Area"
        verbose_name_plural = "Areas"
        db_table = "areas"
        ordering = ["id"]
class Servicio(models.Model):
    servicio = models.CharField(max_length=150,verbose_name="Servicio")
    def __str__(self) -> str:
        return self.servicio
    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        db_table = "servicios"
        ordering = ["id"]
class Cliente(models.Model):
    cliente = models.CharField(max_length=150,verbose_name="Cliente")
    def __str__(self) -> str:
        return self.cliente
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        db_table = "clientes"
        ordering = ["id"]
class Producto(models.Model):
    producto = models.CharField(max_length=255,verbose_name="Producto")
    precio = models.DecimalField(max_digits=9,decimal_places=2,verbose_name="Producto",default=0.00)
    def __str__(self) -> str:
        return self.producto+" "+str(self.precio)
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        db_table = "productos"
        ordering = ["id"]
TURNO=[('DIA', 'DIA'), ('TARDE', 'TARDE'), ('NOCHE', 'NOCHE')]
class Produccion(models.Model):
   
    nombre = models.CharField(max_length=25,verbose_name="Nombre")
    apellido = models.CharField(max_length=25,verbose_name="Apellido")
    dni = models.CharField(max_length=12,verbose_name="Documento")
    turno = models.CharField(max_length=15,choices=TURNO,verbose_name="Turno")
    area = models.ForeignKey(Area,on_delete=models.CASCADE,verbose_name="Area")
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE,verbose_name="Servicio")
    orden_servicio = models.CharField(max_length=150,verbose_name="Orden de Servicio")
    orden_produccion = models.CharField(max_length=150,verbose_name="Orden de Produccion")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE,verbose_name="Cliente")
    fecha = models.DateField(verbose_name="Fecha")
    hora_inicio = models.TimeField(verbose_name="Hora de Inicio")
    hora_salida = models.TimeField(verbose_name="Hora de Salida",null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE,verbose_name="Producto")
    lote = models.CharField(max_length=50,verbose_name="Lote")
    kilos = models.DecimalField(default=0.00, max_digits=9,decimal_places=2, verbose_name="Kilo")
    firma = models.ImageField(upload_to="firmas/",verbose_name="Firma")
    validacion = models.IntegerField(default=0)
    class Meta:
        verbose_name = "Produccion"
        verbose_name_plural = "Producciones"
        db_table = "produccion"
        ordering = ["id"]
    def __str__(self) -> str:
        return self.nombre
class Asistencia(models.Model):
        dni = models.CharField(max_length=12,verbose_name="Documento")
        nombre = models.CharField(max_length=25,verbose_name="Nombre")
        apellidos = models.CharField(max_length=30,verbose_name="Apellidos")
        area = models.ForeignKey(Area,on_delete=models.CASCADE,verbose_name="Area")
        hora_entrada = models.TimeField(verbose_name="Hora Entrada",default=time(0,0,0))
        hora_salida = models.TimeField(verbose_name="Hora Salida",default=time(0,0,0))
        fecha = models.DateField(verbose_name="Fecha", default=date(2023,1,1))
        estado = models.IntegerField(default=0,verbose_name="Estado")
        observacion = models.CharField(max_length=250,default="Ninguna",verbose_name="Obervacion")
        class Meta:
            verbose_name = "Asistencia"
            verbose_name_plural = "Asistencias"
            db_table = "asistencia"
            ordering = ["id"]
        def __str__(self) -> str:
            return self.dni+" "+self.nombre+" "+self.apellidos+" "+str(self.fecha)
class Visitas(models.Model):
    
    dni = models.CharField(max_length=12,verbose_name="DNI")
    nombre = models.CharField(max_length=20,verbose_name="Nombre" )
    apellidos = models.CharField(max_length=30,verbose_name="Apellidos")
    fecha_hora = models.DateTimeField(verbose_name="Fecha de ingreso",default = datetime.now())
    class Meta:
        verbose_name = "Visita"
        verbose_name_plural = "Visitas"
        db_table = "visitas"
        ordering = ["id"]
    def __str__(self) -> str:
        return self.dni+ " "+self.nombre+" "+self.apellidos+" "+str(self.fecha_hora)



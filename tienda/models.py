from django.db import models
from datetime import datetime
# Create your models here.

class Localidad(models.Model):
    nombre = models.CharField(max_length=200)
    cp = models.CharField(max_length=20)
    # metadatos
    class Meta:
        ordering= ["nombre"]
        verbose_name_plural = 'Localidades'
    def __str__(self):
        return '%s, CF: %s' % (self.nombre,self.cp)

class Persona(models.Model):
    num_doc = models.CharField("Nº de documento", max_length=100, primary_key=True)
    nombre = models.CharField("Nombre/s", max_length=200)
    apellido = models.CharField(max_length=200)
    fecha_nac = models.DateField("Fecha de Nacimiento", default=datetime.now)
    telefono = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    direccion = models.CharField(max_length=2000)
    localidad = models.ForeignKey(Localidad, null=True, blank=True, on_delete=models.PROTECT, related_name='persona_localidad')
    # metadatos
    class Meta:
        ordering = ["apellido","nombre"]
    def __str__(self):
        return '%s - %s, %s'%(self.num_doc, self.apellido,self.nombre)

class Cliente(models.Model):
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.PROTECT, related_name='cliente_persona')
    categoria = models.CharField(max_length=200)
    fecha_alta = models.CharField(max_length=200, default=datetime.now)

class Cargo(models.Model):
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.PROTECT, related_name='cargo_persona')
    categoria = models.CharField(max_length=200)
    fecha_alta = models.CharField(max_length=200,  default=datetime.now)

class Empleado(models.Model):
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.PROTECT, related_name='empleado_persona')
    legajo = models.CharField(max_length=2000)
    cargo = models.ForeignKey(Cargo, null=True, blank=True, on_delete=models.PROTECT, related_name='empleado_cargo')
    sector = models.CharField(max_length=200)

class Movimiento(models.Model):
    nombre = models.CharField(max_length=200)
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.PROTECT, related_name='movimiento_cliente')
    numero = models.CharField(max_length=200)
    fecha = models.CharField(max_length=200, default=datetime.now)
    
class Categoria(models.Model):
    id_categoria = models.CharField(max_length=100)
    nombre = models.CharField(max_length=200)
    marca = models.CharField(max_length=200)
    descripcion_categoria = models.CharField(max_length=20000)

class Articulo(models.Model):
    id_art = models.CharField(max_length=100)
    marca = models.CharField(max_length=200)
    descripcion_art = models.CharField(max_length=20000)
    categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.PROTECT, related_name='articulo_categoria')
    stock = models.CharField(max_length=200)
    precio = models.CharField(max_length=200)
    disponible = models.CharField(max_length=2000)
    stock = models.CharField(max_length=200)
    imagen = models.CharField(max_length=900000)


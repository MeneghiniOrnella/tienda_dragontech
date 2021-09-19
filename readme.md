## Paso a paso
1. Diagramar proyecto
2. Abrir XAMPP, iniciar Apache y MySQL
3. Crear Base de datos db_tienda_dragontech
4. Crear usuario en PhpMyAdmin <br>
>user: admin_COM <br>
host: %localhost <br>
password: lulu2021 <br>
5. Desde terminal crear proyecto (evitar modficar nombre)
>django-admin startproject tienda_dragontech<br>
cd tienda_dragontech<br>
python manage.py startapp tienda<br>
6. Abrir proyecto con IDE dragontech_tienda > settings.py
```
INSTALLED_APPS = [
    ... ,
    'tienda',
]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_tienda_dragontech',
        'USER': 'admin_COM',
        'PASSWORD': 'lulu2021',
    }
}
LANGUAGE_CODE = 'es-ar'
```
7. Desde terminal correr servidor
>pip install mysqlclient<br>
python manage.py runserver<br>
8. Crear clases en IDE tienda > models.py, ya tener definidos los campos para luego hacer pocos cambios, se crean las tablas
```
class Localidad(models.Model):
    nombre = models.CharField(max_length=200)
    cp = models.CharField(max_length=20)
    # metadatos
    class Meta:
        ordering: ["nombre"]
        verbose_name_plural = 'Localidades'
    def __str__(self):
        return self.nombre
class Persona(models.Model):
    num_doc = models.CharField("Nº de documento", max_length=100, primary_key=True)
    nombre = models.CharField("Nombre/s", max_length=200)
    apellido = models.CharField(max_length=200)
    fecha_nac = models.CharField("Fecha de Nacimiento", max_length=200)
    telefono = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    direccion = models.CharField(max_length=2000)
    localidad = models.ForeignKey(Localidad, null=True, blank=True, on_delete=models.PROTECT, related_name='persona_localidad')
    # metadatos
    class Meta:
        ordering: ["apellido","nombre"]
    def __str__(self):
        return '%s - %s, %s'%(self.num_doc, self.apellido,self.nombre)
```
9. Para hacer pruebas se debe migrar
>python manage.py makemigrations<br>
10. Para modificar tamaño de imagenes
>pip install django-resized
11. Definir fomularios parar eso se crea en la carpeta tienda > forms.py, los formularios no deben tener el mismo nombre
```
from django.forms import ModelForm
form .models import Localidad, Persona, Cliente, Cargo, Movimiento, Categoria, Articulo
class Localidad(models.Model):
    nombre = models.CharField(max_length=200)
    cp = models.CharField(max_length=20)
    # metadatos
    class Meta:
        ordering= ["nombre"]
        verbose_name_plural = 'Localidades'
    def __str__(self):
        return self.nombre
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
```
12. Crear carpeta templates y templates > tienda > personas.html
```
<table>
    <thead>
        <tr>
            <th>Apellido</th>
            <th>Nombre</th>
            <th>Nº de Documento</th>
            <th>Fecha de Nacimiento</th>
            <th>Teléfono</th>
            <th>Email</th>
            <th>Dirección</th>
            <th>Localidad</th>
        </tr>
    </thead>
    <tbody>
        {{% for persona in personas %}}
        <tr>
            <td>{{ persona.apellido }}</td>
            <td>{{ persona.nombre }}</td>
            <td>{{ persona.num_doc }}</td>
            <td>{{ persona.fecha_nac }}</td>
            <td>{{ persona.telefono }}</td>
            <td>{{ persona.email }}</td>
            <td>{{ persona.direccion }}</td>
            <td>{{ persona.localidad.cp }}</td>
        </tr>
        {{% endfor %}}
    </tbody>
</table>
```
13. Agregar en el archivo tienda_dragontech > urls.py
```
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tienda.urls'))
]
```
14. Creamos el archivo tienda > urls.py
```
from django.urls import path
from .views import persona_listar
urlpatterns = [
    path("personas",persona_listar,name='persona_listar')
]
```
15. Agregamos al archivo tienda_dragontech > urls.py
```
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tienda.urls'))
]
```
16. Se prueba con datos en la tabla
17. Modificamos al archivo tienda_dragontech > models.py
```
class Localidad(models.Model):
    nombre = models.CharField(max_length=200)
    cp = models.CharField(max_length=20)
    # metadatos
    class Meta:
        ordering= ["nombre"]
        verbose_name_plural = 'Localidades'
    def __str__(self):
        return '%s, CF: %s' % (self.nombre,self.cp)
```
18. Se puede añadir estilo a Bootstrap, para eso descargar de la pagina el archivo rar de CSS y JS.<br>
Añadir dragontech_tienda > settings.py
```
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```
Crear carpeta static donde se agregaran las carpetas CSS y JS descargadas de la pagina de Bootstrap<br>
Agrego a los HTML
```
<!DOCTYPE html>
{% load static %}
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Listado de personas</title>
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
    <link rel="stylesheet" href="{% static 'css/bootstrap-theme.css' %}" media="screen">
```
19. Creamos los formularios para agregar información, templates > tienda > personas_form.html
```
    <form method="post" enctype="multipart/form-data" novalidate="">
        {% carf-token %}
        <h1>Persona</h1>
        <label></label> <input type="text">
        <label></label> <input type="text">
        <label></label> <input type="text">
        <label></label> <input type="text">
        <label></label> <input type="text">
        <label></label> <input type="text">
        <label></label> <input type="text">
    </form>
```
20. Modificar archivo tienda > views.py
```
from django.shortcuts import render
from .models import Persona
from .forms import PersonaForm
def nueva_persona(request, template_name="tienda/personas_form.html"):
    if request.method == 'POST':
        pass
    else:
        form = PersonaForm()
    dato = {"form":form}
    return render(request, template_name,dato)
```
21. Modificar tienda > urls.py
```
from django.urls import path
from .views import persona_listar
urlpatterns = [
    path("personas",persona_listar,name='persona_listar'),
    path("nueva_persona",views.nueva_persona,name="nueva_persona")
]
```
22. Se crea el archivo templates > tienda > persona_form.py
```

```
23. 
from django import forms
from django.forms import ModelForm
from django.forms.widgets import DateInput
from .models import Localidad, Persona, Cliente, Cargo, Movimiento, Categoria, Articulo

class LocalidadForm(ModelForm):
    class Meta:
        model = Localidad
        fields = '__all__'

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class CargoForm(ModelForm):
    class Meta:
        model = Cargo
        fields = '__all__'

class MovimientoForm(ModelForm):
    class Meta:
        model = Movimiento
        fields = '__all__'

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class ArticuloForm(ModelForm):
    class Meta:
        model = Articulo
        fields = '__all__'

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'num_doc': forms.TextInput(attrs={'class':'form-control input'}),
            'apellido': forms.TextInput(attrs={'class':'form-control input', 'text-transform':'capitalize','placeholder':'Apellido: Martinez'}),
            'nombre': forms.TextInput(attrs={'class':'form-control input', 'text-transform':'capitalize','placeholder':'Nombre: Jane'}),
            'fecha_nac': DateInput(format='%Y-%m-%d', attrs={'class':'form-control input-sm'}),
            'localidad': forms.Select(attrs={'class':'form-control input'}),
            'email': forms.TextInput(attrs={'class':''}),
        }
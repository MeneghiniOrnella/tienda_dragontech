# Create your views here.

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

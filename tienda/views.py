# Create your views here.

from django.shortcuts import redirect, render
from .models import Persona
from .forms import PersonaForm

def nueva_persona(request, template_name="tienda/personas_form.html"):
    if request.method == 'POST':
        pass
    else:
        form = PersonaForm()
    dato = {"form":form}
    return render(request, template_name,dato)

def modificar_persona(request,pk,template_name='tienda/personas_form.html'):
    persona = Persona.objects.get(num_doc=pk)
    form = PersonaForm(request.post or None, instance = persona)
    if form.is_valid():
        form.save(commit=True)
        return redirect ("persona_listar")
    else:
        print(form.errors)
    datos = ('form':form)
    return render(request, template_name, datos)
    
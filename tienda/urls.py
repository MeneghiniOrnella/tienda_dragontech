from django.urls import path
from .views import persona_listar

urlpatterns = [
    path("personas",persona_listar,name='persona_listar'),
    path("nueva_persona",views.nueva_persona,name="nueva_persona"),
    path("modificar_personas/<int:pk>", views.modoficar_persona, views.modoficar_persona, name="modificar_personas_1")
]
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aula/cadastrar/', views.cadastrar_aula, name='cadastrar_aula'),
    path('aula/consultar/', views.consultar_aulas, name='consultar_aula'),
    path('aula/reservar/', views.reservar_aula, name='reservar_aula'),
]

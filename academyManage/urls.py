from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('criar_aula', views.cadastrar_aula, name='cadastrar_aula'),
    path('ver_aulas', views.consultar_aulas, name='consultar_aula'),
    path('reservar_aula', views.reservar_aula, name='reservar_aula'),
]

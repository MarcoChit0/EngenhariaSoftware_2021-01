from django.urls import path

from . import views

app_name = 'servico'
urlpatterns = [
    path('', views.index, name='index'),
    path('aula/cadastrar/<int:cliente_id>/<int:professor_id>/<int:especialidade_id>/<int:timestamp>/', views.cadastrar_aula, name='cadastrar_aula'),
    path('consulta-medica/cadastrar/<int:cliente_id>/<int:medico_id>/<int:timestamp>/', views.cadastrar_consulta_medica, name='cadastrar_consulta_medica'),
    path('aula/consultar/<int:cliente_id>/', views.consultar_aula, name='consultar_aula'),
    path('consulta-medica/consultar/<int:cliente_id>/', views.consultar_consulta_medica, name='consultar_aula'),
    path('aula/reservar/<int:cliente_id>/<int:aula_id>/', views.reservar_aula, name='reservar_aula'),
]
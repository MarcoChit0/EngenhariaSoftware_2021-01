from django.urls import path

from . import views

app_name = 'servico'
urlpatterns = [
    path('', views.index, name='index'),
    path('aula/gerar-cadastro_aula', views.gerar_cadastro_aula),
    path('aula/cadastrar', views.cadastrar_aula, name='cadastrar_aula'),
    path('consulta-medica/gerar-cadastro-consulta-medica', views.gerar_cadastro_consulta),
    path('consulta-medica/cadastrar', views.cadastrar_consulta_medica,name = 'cadastrar_consulta_medica'),
    path('aula/gerar-consulta/', views.gerar_consulta_aula),
    path('aula/consultar/', views.consultar_aula, name='consultar_aula'),
    path('consulta-medica/gerar-consulta/', views.gerar_consulta_consulta_medica),
    path('consulta-medica/consultar/', views.consultar_consulta_medica, name='consultar_consulta'),
    path('todos/gerar-consulta/', views.gerar_consulta_todos),
    path('todos/consultar/', views.consultar_servicos, name='consultar_servicos'),
    path('aula/reservar/<int:cliente_id>/<int:aula_id>/', views.reservar_aula, name='reservar_aula'),
    path('consulta-medica/reservar/<int:cliente_id>/<int:consulta_medica_id>/', views.reservar_consulta_medica, name='reservar_consulta_medica'),
]
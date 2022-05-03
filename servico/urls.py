from django.urls import path

from . import views

app_name = 'servico'
urlpatterns = [
    path('', views.index, name='index'),
    path('aula/gerar-cadastro_aula', views.Cadastrar.gerar_cadastro_aula),
    path('aula/cadastrar', views.Cadastrar.cadastrar_aula, name='cadastrar_aula'),
    path('consulta-medica/gerar-cadastro-consulta-medica', views.Cadastrar.gerar_cadastro_consulta),
    path('consulta-medica/cadastrar', views.Cadastrar.cadastrar_consulta_medica,name = 'cadastrar_consulta_medica'),
    path('aula/gerar-consulta/', views.Consultar.gerar_consulta_aula),
    path('aula/consultar/', views.Consultar.consultar_aula, name='consultar_aula'),
    path('consulta-medica/gerar-consulta/', views.Consultar.gerar_consulta_consulta_medica),
    path('consulta-medica/consultar/', views.Consultar.consultar_consulta_medica, name='consultar_consulta'),
    path('todos/gerar-consulta/', views.Consultar.gerar_consulta_todos),
    path('todos/consultar/', views.Consultar.consultar_servicos, name='consultar_servicos'),
    path('aula/reservar/efetuar-reserva/', views.Reservar.reservar_aula, name='reservar_aula'),
    path('consulta-medica/reservar/efetuar-reserva/', views.Reservar.reservar_consulta_medica, name='reservar_consulta_medica'),
    path('aula/reservar/', views.Reservar.gerar_formulario_contratar_aula),
    path('consulta-medica/reservar/', views.Reservar.gerar_formulario_contratar_consulta_medica)
]
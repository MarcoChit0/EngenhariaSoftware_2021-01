from django.urls import path

from . import views

app_name = 'servico'
urlpatterns = [
    path('', views.index, name='index'),
    path('aula/cadastrar/<int:professor_id>/<int:especialidade_id>/<int:timestamp>/', views.cadastrar_aula, name='cadastrar_aula'),
    path('consulta-medica/cadastrar/<int:medico_id>/<int:timestamp>/', views.cadastrar_consulta_medica, name='cadastrar_consulta_medica'),
    path('aula/gerar-consulta/', views.gerar_consulta_aula),
    path('aula/consultar/', views.consultar_aula, name='consultar_aula'),
    path('consulta-medica/gerar-consulta/', views.gerar_consulta_consulta_medica),
    path('consulta-medica/consultar/', views.consultar_consulta_medica, name='consultar_consulta'),
    path('todos/gerar-consulta/', views.gerar_consulta_todos),
    path('todos/consultar/', views.consultar_servicos, name='consultar_servicos'),
    path('aula/reservar/efetuar-reserva/', views.reservar_aula, name='reservar_aula'),
    path('consulta-medica/reservar/efetuar-reserva/', views.reservar_consulta_medica, name='reservar_consulta_medica'),
    path('aula/reservar/', views.gerar_formulario_contratar_aula),
    path('consulta-medica/reservar/', views.gerar_formulario_contratar_consulta_medica)
]
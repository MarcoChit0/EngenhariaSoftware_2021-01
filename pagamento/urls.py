from django.urls import path

from . import views

app_name = 'pagamento'
urlpatterns = [
    path('', views.index, name='index'),
    path('cartao/cadastrar/<numero>/<int:saldo>/<int:validade>/<int:CVV>', views.cadastrar_cartao_de_credito, name='cadastrar_cartao_de_credito'),
    path('consulta-medica/cadastrar/<int:medico_id>/<int:timestamp>/', views.cadastrar_consulta_medica, name='cadastrar_consulta_medica'),
    path('aula/consultar/<int:cliente_id>/', views.consultar_aula, name='consultar_aula'),
    path('consulta-medica/consultar/<int:cliente_id>/', views.consultar_consulta_medica, name='consultar_aula'),
    path('aula/reservar/<int:cliente_id>/<int:aula_id>/', views.reservar_aula, name='reservar_aula'),
    path('consulta-medica/reservar/<int:cliente_id>/<int:consulta_medica_id>/', views.reservar_consulta_medica, name='reservar_consulta_medica'),
]
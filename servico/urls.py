from django.urls import path

from . import views

app_name = 'servico'
urlpatterns = [
    path('', views.index, name='index'),
    path('aula/cadastrar/<int:cliente_id>/<int:professor_id>/<int:especialidade_id>/<int:timestamp>/', views.cadastrar_servico, name='cadastrar_aula'),
    path('aula/consultar/<int:cliente_id>/', views.consultar_aula, name='consultar_aula'),
    path('consulta-medica/consultar/<int:cliente_id>/', views.consultar_consulta_medica, name='consultar_aula'),
    path('aula/reservar/<int:cliente_id>/<int:aula_id>/', views.reservar_aula, name='reservar_aula'),
]

''' 
    urlpatterns = [
        path('', views.IndexView.as_view(), name='index'),
        path('<int:pk>/', views.DetailView.as_view(), name='detail'),
        path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
        path('<int:question_id>/vote/', views.vote, name='vote'),
    ]
'''

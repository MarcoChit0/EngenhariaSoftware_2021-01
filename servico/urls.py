from django.urls import path

from . import views

app_name = 'servico'
urlpatterns = [
    path('', views.index, name='index'),
    path('aula/cadastrar/', views.cadastrar_aula, name='cadastrar_aula'),
    path('aula/consultar/', views.consultar_aulas, name='consultar_aula'),
    path('aula/reservar/', views.reservar_aula, name='reservar_aula'),
]

''' 
    urlpatterns = [
        path('', views.IndexView.as_view(), name='index'),
        path('<int:pk>/', views.DetailView.as_view(), name='detail'),
        path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
        path('<int:question_id>/vote/', views.vote, name='vote'),
    ]
'''

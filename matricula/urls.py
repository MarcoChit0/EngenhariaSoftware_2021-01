from django.urls import path

from . import views

app_name = 'matricula'
urlpatterns = [
    path('', views.realizar_matricula, name='realizar-matricula')
]
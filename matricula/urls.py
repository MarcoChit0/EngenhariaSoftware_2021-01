from django.urls import path

from . import views

app_name = 'matricula'
urlpatterns = [
    path('realizar-matricula/<int:cliente_id>/<int:cartao_id>', views.realizar_matricula, name='realizar-matricula')
]
from django.urls import path

from . import views

app_name = 'pagamento'
urlpatterns = [
    path('', views.index, name='index'),
    path('cartao/cadastrar/<str:numero>/<int:saldo>/<int:validade>/<int:cvv>/<int:cliente_id>', views.cadastrar_cartao_de_credito, name='cadastrar_cartao_de_credito'),
    path('realizar/<int:cliente_id>/<int:valor>/<int:cartao_id>', views.realizar_pagamento, name='realizar_pagamento'),
]
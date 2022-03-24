from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/<int:user_id>', views.show_user, name='user'),
    path('test/', views.test, name='test'),
]

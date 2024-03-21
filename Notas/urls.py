from django.urls import path
from . import views

app_name = 'Notas'

urlpatterns = [
    path('', views.index, name='index'),
    path('notas/', views.notas, name='notas'),
]
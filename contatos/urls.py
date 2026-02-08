from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_contatos, name='lista_contatos'),
    path('buscar/', views.buscar_contatos, name='buscar_contatos'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_contatos, name='lista_contatos'),
    path('buscar/', views.buscar_contatos, name='buscar_contatos'),
    path('contato/<int:id>/', views.detalhe_contato, name='detalhe_contato'),
]
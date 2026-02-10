from django.urls import path
from . import views  # Importa as views do app atual

urlpatterns = [
    path('', views.lista_contatos, name='lista_contatos'),
    # Se a função buscar_contatos não existe, use lista_contatos ou outra existente
    # path('buscar/', views.buscar_contatos, name='buscar_contatos'),
    path('buscar/', views.lista_contatos, name='buscar_contatos'),  # Temporário
]
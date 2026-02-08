from django.contrib import admin
from .models import Contato

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'lotacao', 'funcao', 'celular', 'email', 'ativo')
    list_filter = ('lotacao', 'ativo')
    search_fields = ('nome_completo', 'lotacao', 'funcao', 'email')
    list_per_page = 20
    ordering = ('nome_completo',)
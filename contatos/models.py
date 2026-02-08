from django.db import models
from django.contrib.auth.models import User

class Contato(models.Model):
    nome_completo = models.CharField('Nome Completo', max_length=150)
    lotacao = models.CharField('Lotação', max_length=100)
    funcao = models.CharField('Função', max_length=100)
    celular = models.CharField('Celular', max_length=20, blank=True, null=True)
    voip = models.CharField('VOIP/Ramal', max_length=15, blank=True, null=True)
    email = models.EmailField('E-mail', blank=True, null=True)
    ativo = models.BooleanField('Ativo', default=True)
    data_cadastro = models.DateTimeField('Data de Cadastro', auto_now_add=True)
    data_modificacao = models.DateTimeField('Última Modificação', auto_now=True)
    criado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.nome_completo
    
    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'
        ordering = ['nome_completo']
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.core.paginator import Paginator  # ← ADICIONE ESTA LINHA
from .models import Contato  # Se tiver um modelo Contato

def lista_contatos(request):
    # Seu código existente...
    contatos_list = Contato.objects.all()  # Exemplo, ajuste conforme seu código
    paginator = Paginator(contatos_list, 6)  # Agora Paginator está definido
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'contatos/lista.html', {'page_obj': page_obj})
from django.http import HttpResponse
from .models import Contato

def lista_contatos(request):
    # Filtro por lotação, se fornecido
    lotacao_filtro = request.GET.get('lotacao', '')
    
    if lotacao_filtro:
        contatos_list = Contato.objects.filter(ativo=True, lotacao__icontains=lotacao_filtro).order_by('nome_completo')
    else:
        contatos_list = Contato.objects.filter(ativo=True).order_by('nome_completo')
    
    # Paginação: 6 contatos por página
    paginator = Paginator(contatos_list, 6)
    page_number = request.GET.get('page')
    contatos = paginator.get_page(page_number)
    
    # Pegar lista única de lotações para o filtro
    lotacoes = Contato.objects.filter(ativo=True).values_list('lotacao', flat=True).distinct().order_by('lotacao')
    
    return render(request, 'contatos/lista.html', {
        'contatos': contatos,
        'total': contatos_list.count(),
        'lotacoes': lotacoes,
        'lotacao_filtro': lotacao_filtro
    })
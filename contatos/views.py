from django.http import HttpResponse
from .models import Contato

def lista_contatos(request):
    # Tente contar os contatos
    total = Contato.objects.count()
    return HttpResponse(f"Total de contatos: {total}")

def buscar_contatos(request):
    return HttpResponse("Busca")

from django.shortcuts import render, get_object_or_404

def detalhe_contato(request, id):
    contato = get_object_or_404(Contato, id=id, ativo=True)
    return render(request, 'contatos/detalhe.html', {'contato': contato})
import pandas as pd
from django.http import HttpResponse
from datetime import datetime

def exportar_contatos(request, formato='excel'):
    contatos = Contato.objects.filter(ativo=True).values(
        'nome_completo', 'lotacao', 'funcao', 'celular', 'voip', 'email'
    )
    
    df = pd.DataFrame(contatos)
    
    if formato == 'excel':
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = f'attachment; filename="contatos_{datetime.now().strftime("%Y%m%d_%H%M%S")}.xlsx"'
        df.to_excel(response, index=False)
    elif formato == 'csv':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="contatos_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv"'
        df.to_csv(response, index=False)
    else:
        return HttpResponse("Formato não suportado", status=400)
    
    return response
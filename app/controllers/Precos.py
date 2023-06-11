from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse

from app.models import Precos, Tipos
from app.forms.Precos import PrecoForm
from app.tools import utc_to_local

@login_required
def create(req):
    form = PrecoForm()
    title = "Cadastro de Preco"
    message = None
    var_btn_value = "CADASTRAR"
    
    if ( req.POST ):
        form = PrecoForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            form = PrecoForm()
            message = "Preco cadastrado com sucesso!"
        else:
            message = "Verifique os erros!"
            
    return render(req,'form.html', {
        "form": form, 
        "message": message, 
        "var_btn_value" : var_btn_value,
        "title": title
    })

@login_required
def lista(req):
    query = Tipos.objects.filter(fk_status__descricao = 'Ativo')
    data = [["TIPO DE VEICULO", "PREÇO POR HORA", "PREÇO MENSAL", "ULTIMA ATUALIZAÇÃO"]]
    for row in query:
        tipo_de_veiculo = row.descricao
        try: 
            p = Precos.objects.get(fk_tipo = row, fk_status = 'Ativo')
            preco_por_hora = str("R$ %.2f" % float(p.por_hora)).replace('.', ',')
            preco_mensal = str("R$ %.2f" % float(p.por_mensalidade)).replace('.', ',')
            ultima_atualizacao = utc_to_local(p.created_at).strftime("%d/%m/%Y %H:%M:%S")
        except: 
            preco_por_hora = "---"
            preco_mensal  = "---"
            ultima_atualizacao  = "---"
        
        data.append(tipo_de_veiculo, preco_por_hora, preco_mensal, ultima_atualizacao)
    
    return JsonResponse(data={"data":data})

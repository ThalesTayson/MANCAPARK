from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils import timezone

from app.models import Estacionamento, Registros, Precos
from app.forms.Estacionamento import EstacionamentoForm
from app.tools import calculaTempo_em_hour_e_min, calculaTempo, utc_to_local

@login_required
def update(req):
    form = EstacionamentoForm()
    title = "Veiculos no Estacionamento"
    message = None
    var_btn_value = "REGISTRAR"
    
    if ( req.POST ):
        form = EstacionamentoForm(req.POST, req.FILES)
        if form.is_valid():
            form.save(req.user)
            form = EstacionamentoForm()
            message = "Movimentação registrada com sucesso!"
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
    query = Estacionamento.objects.filter( fk_status__descricao = 'Ativo')
    data = [["DATA/HORA DA ENTRADA","VEICULO", "CLIENTE", "TEMPO (h)", "VALOR"]]
    for row in query:
        veiculo = str(row.fk_veiculo)
        cliente = str(row.fk_veiculo.fk_cliente)
        reg_entrada = Registros.objects.get(
            fk_veiculo = row.fk_veiculo,
            fk_tipoRegistro__descricao = 'Entrada', 
            fk_status__descricao = 'Ativo'
        )
        data_hora_da_entrada = utc_to_local(reg_entrada.created_at).strftime("%d/%m/%Y %H:%M:%S")
        tempo = calculaTempo_em_hour_e_min(reg_entrada.created_at, timezone.now())
        valor = "---"
        if row.fk_veiculo.fk_status == 'Inativo':
            preco = Precos.objects.get(
                    fk_status__descricao = 'Ativo', 
                    fk_tipo = row.fk_veiculo.fk_modelo.fk_tipo
                )
            tempoP= calculaTempo(reg_entrada.created_at, timezone.now())
            valor = float(preco.por_hora * tempoP)
            valor = str("R$ %.2f" % float(valor)).replace('.', ',')
        data.append([data_hora_da_entrada, veiculo, cliente, tempo, valor])
    
    return JsonResponse(data={"data":data})
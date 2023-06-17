from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils import timezone

from app.models import Estacionamento, Registros, Precos
from app.forms.Estacionamento import EntradaForm, SaidaForm
from app.tools import calculaTempo_em_hour_e_min, calculaTempo, utc_to_local, formToJson

@login_required
def entrada(req):
    form = EntradaForm()
    title = "Registrar Entrada"
    message = {}
    var_btn_value = "REGISTRAR"
    
    if ( req.POST ):
        form = EntradaForm(req.POST, req.FILES)
        if form.is_valid():
            form.save(req.user)
            form = EntradaForm()
            message = {"status": "success", "msg": "Entrada registrada com sucesso!"}
        else:
            try: message = {"status": "error", "msg": form.errors.get("__all__").as_text()}
            except: message = {"status": "error", "msg": "Verifique os campos!"}
    
    data = {
        "form": formToJson(form),
        "message": message, 
        "var_btn_value" : var_btn_value,
        "title": title
    }

    return JsonResponse(data=data)

@login_required
def saida(req):
    form = SaidaForm()
    title = "Registrar Saida"
    message = {}
    var_btn_value = "REGISTRAR"
    
    if ( req.POST ):
        form = SaidaForm(req.POST, req.FILES)
        if form.is_valid():
            form.save(req.user)
            form = SaidaForm()
            message = {"status": "success", "msg": "Saida registrada com sucesso!"}
        else:
            try: message = {"status": "error", "msg": form.errors.get("__all__").as_text()}
            except: message = {"status": "error", "msg": "Verifique os campos!"}

    data = {
        "form": formToJson(form),
        "message": message, 
        "var_btn_value" : var_btn_value,
        "title": title
    }
    
    return JsonResponse(data=data)
    
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
        if row.fk_veiculo.fk_status.descricao == 'Inativo':
            preco = Precos.objects.get(
                    fk_status__descricao = 'Ativo', 
                    fk_tipo = row.fk_veiculo.fk_modelo.fk_tipo
                )
            tempoP= calculaTempo(reg_entrada.created_at, timezone.now())
            valor = float(preco.por_hora * tempoP)
            valor = str("R$ %.2f" % float(valor)).replace('.', ',')
        data.append([data_hora_da_entrada, veiculo, cliente, tempo, valor])
    
    return JsonResponse(data={"data":data})
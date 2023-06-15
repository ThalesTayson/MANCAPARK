from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse

from app.models import Veiculos
from app.forms.Veiculos import VeiculoForm, StatusVeiculoForm
from app.tools import utc_to_local, formToJson

@login_required
def create(req):
    form = VeiculoForm()
    title = "Cadastro de Veiculo"
    message = None
    var_btn_value = "CADASTRAR"
    
    if ( req.POST ):
        form = VeiculoForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            form = VeiculoForm()
            message = {"status": "success", "msg": "Veiculo cadastrado com sucesso!"}
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
def update(req, id):
    model = Veiculos.objects.get(id = id)
    form = VeiculoForm(instance = model)
    title = "Atualizando Veiculo"
    message = None
    var_btn_value = "SALVAR"
    
    if ( req.POST ):
        form = VeiculoForm(req.POST, req.FILES, instance = model)
        if form.is_valid():
            form.save()
            message = {"status": "success", "msg": "Veiculo atualizado com sucesso!"}
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
def status_update(req, id):
    model = Veiculos.objects.get(id = id)
    form = StatusVeiculoForm(instance = model)
    title = "Atualizando Status do Veiculo"
    message = None
    var_btn_value = "ATUALIZAR"
    
    if ( req.POST ):
        form = StatusVeiculoForm(req.POST, req.FILES, instance = model)
        if form.is_valid():
            form.save()
            message = {"status": "success", "msg": "Status atualizado com sucesso!"}
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
    query = Veiculos.objects.filter()
    data = [["ID", "PLACA", "CLIENTE", "TIPO DE VEICULO", "MARCA", "MODELO", "DATA DE CADASTRO", "ULTIMA ATUALIZAÇÃO", "STATUS", "..."]]
    for row in query:
        id = str(row.pk)
        placa = row.placa
        try: cliente = row.fk_cliente.primeiro_nome + ' ' + row.fk_cliente.ultimo_nome
        except: cliente = "---"
        tipo_de_veiculo = row.fk_modelo.fk_tipo.descricao
        marca = row.fk_modelo.fk_marca.descricao
        modelo = row.fk_modelo.descricao
        data_de_cadastro = utc_to_local(row.created_at).strftime("%d/%m/%Y %H:%M:%S")
        ultima_atualizacao = utc_to_local(row.updated_at).strftime("%d/%m/%Y %H:%M:%S")
        status = row.fk_status.descricao
        
        menu = [
            {"value": "ATUALIZAR CADASTRO", 'link': f"veiculos/{id}/update"},
            {"value": "ATUALIZAR STATUS", 'link': f"veiculos/{id}/status/update"},
        ]
        
        data.append([id, placa, cliente, tipo_de_veiculo, marca, modelo, data_de_cadastro, ultima_atualizacao, status, menu])
    
    return JsonResponse(data={"data":data})

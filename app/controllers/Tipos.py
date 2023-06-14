from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse

from app.models import Tipos
from app.forms.Tipos import TipoForm, StatusTipoForm
from app.tools import utc_to_local, formToJson

@login_required
def create(req):
    form = TipoForm()
    title = "Cadastro de Tipo de veiculo"
    message = None
    var_btn_value = "CADASTRAR"
    
    if ( req.POST ):
        form = TipoForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            form = TipoForm()
            message = {"status": "info", "msg": "Tipo de Veiculo cadastrado com sucesso!"}
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
    model = Tipos.objects.get(id = id)
    form = TipoForm(instance = model)
    title = "Atualizando Tipo de Veiculo"
    message = None
    var_btn_value = "SALVAR"
    
    if ( req.POST ):
        form = TipoForm(req.POST, req.FILES, instance = model)
        if form.is_valid():
            form.save()
            message = {"status": "info", "msg": "Tipo de Veiculo atualizado com sucesso!"}
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
    model = Tipos.objects.get(id = id)
    form = StatusTipoForm(instance = model)
    title = "Atualizando Status de Tipo de Veiculo"
    message = None
    var_btn_value = "ATUALIZAR"
    
    if ( req.POST ):
        form = StatusTipoForm(req.POST, req.FILES, instance = model)
        if form.is_valid():
            form.save()
            message = {"status": "info", "msg": "Status atualizado com sucesso!"}
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
    query = Tipos.objects.filter()
    data = [["ID", "DESCRICÃO", "DATA DE CADASTRO", "ULTIMA ATUALIZAÇÃO", "STATUS", "..."]]
    for row in query:
        id = str(row.pk)
        descricao = row.descricao
        data_de_cadastro = utc_to_local(row.created_at).strftime("%d/%m/%Y %H:%M:%S")
        ultima_atualizacao = utc_to_local(row.updated_at).strftime("%d/%m/%Y %H:%M:%S")
        status = row.fk_status.descricao
        
        menu = [
            {"value": "ATUALIZAR CADASTRO", 'link': f"tipos/{id}/update"},
            {"value": "ATUALIZAR STATUS", 'link': f"tipos/{id}/status/update"},
        ]
        
        data.append([id, descricao, data_de_cadastro, ultima_atualizacao, status, menu])
    
    return JsonResponse(data={"data":data})

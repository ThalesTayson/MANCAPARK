from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse

from app.models import Marcas
from app.forms.Marcas import MarcaForm, StatusMarcaForm
from app.tools import utc_to_local, formToJson

@login_required
def create(req):
    form = MarcaForm()
    title = "Cadastro de Marca de Veiculo"
    message = {}
    var_btn_value = "CADASTRAR"
    
    if ( req.POST ):
        form = MarcaForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            form = MarcaForm()
            message = {"status": "info", "msg": "Marca de Veiculo cadastrado com sucesso!"}
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
    model = Marcas.objects.get(id = id)
    form = MarcaForm(instance = model)
    title = "Atualizando Marca de Veiculo"
    message = None
    var_btn_value = "SALVAR"
    
    if ( req.POST ):
        form = MarcaForm(req.POST, req.FILES, instance = model)
        if form.is_valid():
            form.save()
            message = {"status": "info", "msg": "Marca de Veiculo atualizada com sucesso!"}
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

def status_update(req, id):
    model = Marcas.objects.get(id = id)
    form = StatusMarcaForm(instance = model)
    title = "Atualizando Status de Marca"
    message = None
    var_btn_value = "ATUALIZAR"
    
    if ( req.POST ):
        form = StatusMarcaForm(req.POST, req.FILES, instance = model)
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
    query = Marcas.objects.filter()
    data = [["ID", "DESCRICÃO", "DATA DE CADASTRO", "ULTIMA ATUALIZAÇÃO", "STATUS", "..."]]
    for row in query:
        id = str(row.pk)
        descricao = row.descricao
        data_de_cadastro = utc_to_local(row.created_at).strftime("%d/%m/%Y %H:%M:%S")
        ultima_atualizacao = utc_to_local(row.updated_at).strftime("%d/%m/%Y %H:%M:%S")
        status = row.fk_status.descricao
        
        menu = [
            {"value": "ATUALIZAR CADASTRO", 'link': f"marcas/{id}/update"},
            {"value": "ATUALIZAR STATUS", 'link': f"marcas/{id}/status/update"},
        ]
        
        data.append([id, descricao, data_de_cadastro, ultima_atualizacao, status, menu])
    
    return JsonResponse(data={"data":data})

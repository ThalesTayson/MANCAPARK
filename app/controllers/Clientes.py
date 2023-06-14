from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse

from app.models import Clientes
from app.forms.Clientes import ClienteForm
from app.tools import utc_to_local, maskTelefone, formToJson

@login_required
def create(req):
    form = ClienteForm()
    title = "Cadastro de Cliente"
    message = {}
    var_btn_value = "CADASTRAR"
    
    if ( req.POST ):
        form = ClienteForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            form = ClienteForm()
            message = {"status": "info", "msg": "Cliente cadastrado com sucesso!"}
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
    model = Clientes.objects.get(id = id)
    form = ClienteForm(instance = model)
    title = "Atualizando Cliente"
    message = {}
    var_btn_value = "SALVAR"
    
    if ( req.POST ):
        form = ClienteForm(req.POST, req.FILES, instance = model)
        if form.is_valid():
            form.save()
            message = {"status": "info", "msg": "Cliente atualizado com sucesso!"}
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
    query = Clientes.objects.filter()
    data = [["ID", "NOME COMPLETO", "EMAIL", "TELEFONE", "DATA DE CADASTRO", "ULTIMA ATUALIZAÇÃO", "..."]]
    for row in query:
        id = str(row.pk)
        nome_completo = "{} {}".format(row.primeiro_nome, row.ultimo_nome)
        email = row.email
        telefone = maskTelefone(row.telefone)
        data_de_cadastro = utc_to_local(row.created_at).strftime("%d/%m/%Y %H:%M:%S")
        ultima_atualizacao = utc_to_local(row.updated_at).strftime("%d/%m/%Y %H:%M:%S")
        
        menu = [
            {"value": "ATUALIZAR CADASTRO", 'link': f"clientes/{id}/update"}
        ]
        
        data.append([id, nome_completo, email, telefone, data_de_cadastro, ultima_atualizacao, menu])
    
    return JsonResponse(data={"data":data})
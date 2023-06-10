from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse

from app.models import Tipos
from app.forms.Tipos import TipoForm, StatusTipoForm

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
            message = "Tipo de Veiculo cadastrado com sucesso!"
        else:
            message = "Verifique os erros!"
            
    return render(req,'form.html', {
        "form": form, 
        "message": message, 
        "var_btn_value" : var_btn_value,
        "title": title
    })

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
            message = "Tipo de Veiculo atualizado com sucesso!"
        else:
            message = "Verifique os erros!"
            
    return render(req,'form.html', {
        "form": form, 
        "message": message, 
        "var_btn_value" : var_btn_value,
        "title": title
    })

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
            message = "Status atualizado com sucesso!"
        else:
            message = "Verifique os erros!"
            
    return render(req,'form.html', {
        "form": form, 
        "message": message, 
        "var_btn_value" : var_btn_value,
        "title": title
    })
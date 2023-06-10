from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse

from app.models import Modelos
from app.forms.Modelos import ModeloForm, StatusModeloForm

@login_required
def create(req):
    form = ModeloForm()
    title = "Cadastro de Modelo de Veiculo"
    message = None
    var_btn_value = "CADASTRAR"
    
    if ( req.POST ):
        form = ModeloForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            form = ModeloForm()
            message = "Modelo de Veiculo cadastrado com sucesso!"
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
    model = Modelos.objects.get(id = id)
    form = ModeloForm(instance = model)
    title = "Atualizando Modelo de Veiculo"
    message = None
    var_btn_value = "SALVAR"
    
    if ( req.POST ):
        form = ModeloForm(req.POST, req.FILES, instance = model)
        if form.is_valid():
            form.save()
            message = "Modelo de Veiculo atualizado com sucesso!"
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
    model = Modelos.objects.get(id = id)
    form = StatusModeloForm(instance = model)
    title = "Atualizando Status de Modelo de Veiculo"
    var_btn_value = "ATUALIZAR"
    
    if ( req.POST ):
        form = StatusModeloForm(req.POST, req.FILES, instance = model)
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
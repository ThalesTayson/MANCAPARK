from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse

from app.models import Veiculos
from app.forms.Veiculos import VeiculoForm, StatusVeiculoForm

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
            message = "Veiculo cadastrado com sucesso!"
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
    model = Veiculos.objects.get(id = id)
    form = VeiculoForm(instance = model)
    title = "Atualizando Veiculo"
    message = None
    var_btn_value = "SALVAR"
    
    if ( req.POST ):
        form = VeiculoForm(req.POST, req.FILES, instance = model)
        if form.is_valid():
            form.save()
            message = "Veiculo atualizado com sucesso!"
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
    model = Veiculos.objects.get(id = id)
    form = StatusVeiculoForm(instance = model)
    title = "Atualizando Status do Veiculo"
    message = None
    var_btn_value = "ATUALIZAR"
    
    if ( req.POST ):
        form = StatusVeiculoForm(req.POST, req.FILES, instance = model)
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
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse

from app.models import Clientes
from app.forms.Clientes import ClienteForm

@login_required
def create(req):
    form = ClienteForm()
    title = "Cadastro de Cliente"
    message = None
    var_btn_value = "CADASTRAR"
    
    if ( req.POST ):
        form = ClienteForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            form = ClienteForm()
            message = "Cliente cadastrado com sucesso!"
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
    model = Clientes.objects.get(id = id)
    form = ClienteForm(instance = model)
    title = "Atualizando Cliente"
    message = None
    var_btn_value = "SALVAR"
    
    if ( req.POST ):
        form = ClienteForm(req.POST, req.FILES, instance = model)
        if form.is_valid():
            form.save()
            message = "Cliente atualizado com sucesso!"
        else:
            message = "Verifique os erros!"
            
    return render(req,'form.html', {
        "form": form, 
        "message": message, 
        "var_btn_value" : var_btn_value,
        "title": title
    })
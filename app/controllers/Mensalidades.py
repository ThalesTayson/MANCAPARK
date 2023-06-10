from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse

from app.models import Clientes
from app.forms.Mensalidades import MesalidadeForm, InativarClienteForm

@login_required
def create(req):
    form = MesalidadeForm()
    title = "Cadastro de Pagamento de Mensalidade"
    message = None
    var_btn_value = "CADASTRAR"
    
    if ( req.POST ):
        form = MesalidadeForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            form = MesalidadeForm()
            message = "Pagamento cadastrado com sucesso!"
        else:
            message = "Verifique os erros!"
            
    return render(req,'form.html', {
        "form": form, 
        "message": message, 
        "var_btn_value" : var_btn_value,
        "title": title
    })

@login_required
def cliente_inativar(req, id):
    model = Clientes.objects.get(id = id)
    form = InativarClienteForm(instance = model)
    title = "Inativar Cliente"
    message = None
    var_btn_value = "INATIVAR"
    
    if ( req.POST ):
        form = InativarClienteForm(req.POST, req.FILES, instance = model)
        if form.is_valid():
            form.save()
            message = "Cliente Inativado com sucesso!"
        else:
            message = "Verifique os erros!"
            
    return render(req,'form.html', {
        "form": form, 
        "message": message, 
        "var_btn_value" : var_btn_value,
        "title": title
    })
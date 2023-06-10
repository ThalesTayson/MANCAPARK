from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse

from app.models import Estacionamento
from app.forms.Estacionamento import EstacionamentoForm

@login_required
def update(req):
    form = EstacionamentoForm()
    title = "Veiculos no Estacionamento"
    message = None
    var_btn_value = "REGISTRAR"
    
    if ( req.POST ):
        form = EstacionamentoForm(req.POST, req.FILES)
        if form.is_valid():
            form.save(req.user)
            form = EstacionamentoForm()
            message = "Movimentação registrada com sucesso!"
        else:
            message = "Verifique os erros!"
            
    return render(req,'form.html', {
        "form": form, 
        "message": message, 
        "var_btn_value" : var_btn_value,
        "title": title
    })
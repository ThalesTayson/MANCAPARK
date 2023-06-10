from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse

from app.models import Precos
from app.forms.Precos import PrecoForm

@login_required
def create(req):
    form = PrecoForm()
    title = "Cadastro de Preco"
    message = None
    var_btn_value = "CADASTRAR"
    
    if ( req.POST ):
        form = PrecoForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            form = PrecoForm()
            message = "Preco cadastrado com sucesso!"
        else:
            message = "Verifique os erros!"
            
    return render(req,'form.html', {
        "form": form, 
        "message": message, 
        "var_btn_value" : var_btn_value,
        "title": title
    })
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils import timezone

from app.models import Clientes, Mensalidades
from app.forms.Mensalidades import MesalidadeForm, InativarClienteForm
from app.tools import utc_to_local, formToJson

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
            message = {"status": "info", "msg": "Pagamento cadastrado com sucesso!"}
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
            message = {"status": "info", "msg": "Cliente Inativado com sucesso!"}
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
    now = timezone.now().replace(hour=0,minute=0,second=0,microsecond=0)
    limitPagamento = now - timezone.timedelta(days=31)
    query = Mensalidades.objects.filter(
        fk_cliente__fk_status__descricao = 'Ativo',
        fk_pagamento__created_at__gte = limitPagamento
    )
    data = [["CLIENTE", "DATA DO PAGAMENTO", "TIPOS INCLUSO", "VALOR PAGO", "..."]]
    for row in query:
        cliente = str(row.fk_cliente)
        data_do_pagamento = utc_to_local(row.fk_pagamento.created_at).strftime("%d/%m/%Y")
        tipos_incluso = ""
        for tp in row.fk_tipos.filter():
            if tipos_incluso == "":
                tipos_incluso += tp.descricao
            else:
                tipos_incluso += ", {}".format(tp.descricao)
    
        valor_pago = str("R$ %.2f" % float(row.fk_pagamento.valor)).replace('.', ',')
        
        menu = [
            {"value": "INATIVAR", 'link': f"mensalidades/cliente/{row.fk_cliente.pk}/inativar"},
        ]
        
        data.append([cliente, data_do_pagamento, tipos_incluso, valor_pago, menu])
    
    return JsonResponse(data={"data":data})
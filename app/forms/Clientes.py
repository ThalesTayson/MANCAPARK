from django import forms
from django.forms import Form, ModelForm
from app.models import Clientes, Status, Veiculos, Mensalidades, Pagamentos, Precos, Tipos

class ClienteForm(ModelForm):
    class Meta:
        model = Clientes
        fields = ['primeiro_nome', 'ultimo_nome', 'email', 'telefone']
        
class StatusClienteForm(Form):
    fk_status = forms.ModelChoiceField(queryset=Status.objects)
    fk_cliente = forms.ModelChoiceField(queryset=Clientes.objects)
    fk_tipos = forms.ModelChoiceField(queryset=Tipos.objects)
    
    def save(self):
        cliente = self.cleaned_data['fk_cliente']
        cliente.fk_status = self.cleaned_data['fk_status']
        
        if cliente.fk_status.descricao == 'Inativo':
            for veiculo in Veiculos.objects.filter(fk_cliente = cliente):
                veiculo.fk_status = self.cleaned_data['fk_status']
                veiculo.save()
        else:
            pag = Pagamentos()
            precos = Precos.objects.filter(
                    fk_status__descricao = 'Ativo',
                    fk_tipo__in = self.cleaned_data['fk_tipos']
            )
            valor = 0
            for p in precos: valor += p.por_mensalidade
            valor = valor / len(precos)
            
            pag.valor = valor
            pag.fk_preco.add(precos)
            pag.save()
            
            mens = Mensalidades()
            
            mens.fk_cliente = cliente
            mens.fk_pagamento = pag
            mens.save()
            
        cliente.save()
        
        return cliente
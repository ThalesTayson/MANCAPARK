from django import forms
from django.forms import Form, ModelForm
from app.models import Precos

class PrecoForm(ModelForm):
    class Meta:
        model = Precos
        fields = ['fk_tipo', 'por_mensalidade', 'por_hora']
    
class StatusClienteForm(Form):
    fk_status = forms.ModelChoiceField(queryset=Status.objects)
    fk_cliente = forms.ModelChoiceField(queryset=Clientes.objects)
    
    def save(self):
        cliente = self.cleaned_data['fk_cliente']
        cliente.fk_status = self.cleaned_data['fk_status']
        cliente.save()
        
        if cliente.fk_status.descricao == 'Inativo':
            for veiculo in Veiculos.objects.filter(fk_cliente = cliente):
                veiculo.fk_status = self.cleaned_data['fk_status']
                veiculo.save()
        else:
            pag = Pagamentos()
            preco = Precos.objects.get(
                    fk_status__descricao = 'Ativo'
            )

            pag.valor = preco.por_mensalidade
            pag.fk_preco = preco
            pag.save()
            
            mens = Mensalidades()
            
            mens.fk_cliente = cliente
            mens.fk_pagamento = pag
            mens.save()
            
        return cliente
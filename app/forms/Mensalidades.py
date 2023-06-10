from django import forms
from django.forms import ModelForm
from app.models import Clientes, Veiculos, Status, Mensalidades, Pagamentos, Precos, Tipos

class MesalidadeForm(ModelForm):
    fk_tipos = forms.ModelChoiceField(queryset=Tipos.objects.filter(fk_status__descricao = 'Ativo'))
    
    class Meta:
        model = Mensalidades
        fields = ['fk_cliente', 'fk_tipos']
    
    def getValor(self):
        precos = Precos.objects.filter(
                fk_status__descricao = 'Ativo',
                fk_tipo__in = [self.cleaned_data['fk_tipos']]
        )
        
        valor = 0
        for p in precos: valor += p.por_mensalidade
        valor = valor / len(precos)
        
        print(precos)
        return precos, valor
    
    def save(self, ):
        data = self.instance
        cliente = data.fk_cliente
        cliente.fk_status = Status.objects.get(descricao = 'Ativo')
        pag = Pagamentos()
        
        precos, valor = self.getValor()
        
        pag.valor = valor
        pag.save()
        pag.fk_preco.set(precos)
        
        cliente.save()
        
        data.fk_pagamento = pag
        data.save()
        
        return data

class InativarClienteForm(ModelForm):
    class Meta:
        model = Clientes
        fields = []
    
    def clean(self) -> dict[str, any]:
        data = super().clean()
        if self.instance.fk_status.descricao == 'Inativo':
            raise forms.ValidationError('Cliente já encontra-se inativado',
                                        code='cliente_inativa')
            
        return data
    
    def save(self):
        data = super().save(False)
        data.fk_status = Status.objects.get(descricao = 'Inativo')
        data.save()
        
        for veiculo in Veiculos.objects.filter(fk_cliente = data):
            veiculo.fk_status = self.cleaned_data['fk_status']
            veiculo.save()
        
        return data
    
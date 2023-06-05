from django import forms
from django.forms import Form, ModelForm
from app.models import Clientes, Status, Veiculos

class ClienteForm(ModelForm):
    class Meta:
        model = Clientes
        fields = ['primeiro_nome', 'ultimo_nome', 'email', 'telefone']
        
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
        
        return cliente
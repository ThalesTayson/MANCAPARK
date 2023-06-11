from django import forms
from django.forms import ModelForm
from app.models import Veiculos, Modelos, Clientes

class VeiculoForm(ModelForm):
    fk_modelo = forms.ModelChoiceField(queryset=Modelos.objects.filter(fk_status__descricao = 'Ativo'), label= 'Modelo e Marca do Veiculo')
    fk_cliente = forms.ModelChoiceField(queryset=Clientes.objects, label= 'Cliente')
    
    class Meta:
        model = Veiculos
        fields = ['placa', 'fk_modelo', 'fk_cliente']

class StatusVeiculoForm(ModelForm):
    
    class Meta:
        model = Veiculos
        fields = ['fk_status']

    def clean(self) -> dict[str, any]:
        data = super().clean()
        status_set = data.get("fk_status").descricao
        status_cliente = self.instance.fk_cliente.fk_status.descricao
        
        if status_set == 'Ativo' and status_cliente == 'Inativo'> 0:
            raise forms.ValidationError('Não é possível ativar um veiculo de cliente inativado, primeiro ative novamente o cliente.',
                                        code='cliente_inativo')
    
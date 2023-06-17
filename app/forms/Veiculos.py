from django import forms
from django.forms import ModelForm
from app.models import Veiculos, Modelos

class VeiculoForm(ModelForm):
    
    class Meta:
        model = Veiculos
        fields = ['placa', 'fk_modelo', 'fk_cliente']
        
    def __init__(self, *args, **kwargs):
        super(VeiculoForm, self).__init__(*args, **kwargs)
        self.fields['fk_modelo'].queryset = Modelos.objects.filter(fk_status__descricao = 'Ativo')
        
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
    
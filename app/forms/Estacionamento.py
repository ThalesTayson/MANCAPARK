from django import forms
from django.forms import ModelForm
from app.models import Registros, Estacionamento, Veiculos, Status

class EstacionamentoForm(ModelForm):
    fk_veiculo = forms.ModelChoiceField(queryset=Veiculos.objects.filter(fk_status__descricao = 'Ativo'))
    
    class Meta:
        model = Registros
        fields = ['fk_tipoRegistro', 'fk_veiculo', 'fk_usuario']
    
    def clean(self) -> dict[str, any]:
        data = super().clean()
        tp_reg = data.get("fk_tipoRegistro")
        veiculo = data.get("fk_veiculo")
        ests = Estacionamento.objects.filter(fk_veiculo = veiculo)
        
        if len(ests) > 0:
            if ests[0].fk_status.descricao == 'Ativo' and tp_reg.descricao == 'Entrada':
                raise forms.ValidationError('Veiculo já se encontra no Estacionamento!',
                                        code='veiculo_ativo_no_estacionamento')
            if ests[0].fk_status.descricao == 'Inativo' and tp_reg.descricao == 'Saida':
                raise forms.ValidationError('Veiculo já saiu do Estacionamento!',
                                        code='veiculo_inativo_no_estacionamento')
        
        return data
                
    def save(self):
        data =  super().save(False)
        tp_reg = data.fk_tipoRegistro.descricao
        
        status = Status.objects.get(
            descricao = 'Ativo' if tp_reg == 'Entrada' else 'Inativo'
        )
        
        try:
            est = Estacionamento.objects.get(fk_veiculo=data.fk_veiculo)
        except:
            est = Estacionamento()
            est.fk_veiculo = data.fk_veiculo
        
        est.fk_status = status
        
        est.save()
        data.save()
        return data
        
    
from django import forms
from django.forms import ModelForm
from app.models import Registros, Estacionamento, Veiculos, Status

class EstacionamentoForm(ModelForm):
    fk_veiculo = forms.ModelChoiceField(queryset=Veiculos.objects.filter(fk_status__descricao = 'Ativo'))
    
    class Meta:
        model = Registros
        fields = ['fk_tipoRegistro', 'fk_veiculo', 'fk_usuario']
    
    def save(self):
        data =  super().save(False)
        tp_reg = data.instance.fk_tipoRegistro.descricao
        
        status = Status.objects.get(
            descricao = 'Ativo' if tp_reg == 'Entrada' else 'Inativo'
        )
        
        try:
            est = Estacionamento.objects.get(fk_veiculo=data.instance.fk_veiculo)
        except:
            est = Estacionamento()
            est.fk_veiculo = data.instance.fk_veiculo
        
        est.fk_status = status
        
        est.save(True)
        return data.save(True)
        
    
from django import forms
from django.forms import ModelForm
from app.models import Modelos, Tipos, Marcas

class ModeloForm(ModelForm):
    
    class Meta:
        model = Modelos
        fields = ['descricao', 'fk_tipo', 'fk_marca']
        
    def __init__(self, *args, **kwargs):
        super(ModeloForm, self).__init__(*args, **kwargs)
        self.fields['fk_tipo'].queryset = Tipos.objects.filter(fk_status__descricao = 'Ativo')
        self.fields['fk_marca'].queryset = Marcas.objects.filter(fk_status__descricao = 'Ativo')
        
class StatusModeloForm(ModelForm):
    
    class Meta:
        model = Modelos
        fields = ['fk_status']
    
    def clean(self) -> dict[str, any]:
        data = super().clean()
        status_set = data.get("fk_status").descricao
        status_tipo = self.instance.fk_tipo.fk_status.descricao
        status_marca = self.instance.fk_marca.fk_status.descricao
        
        if status_set == 'Ativo' and (status_tipo == 'Inativo' or status_marca == 'Inativo'):
            raise forms.ValidationError('Não é possível ativar um modelo de veiculo com tipo e/ou marca inativados, primeiro ative novamente tipo e/ou marca de veiculo.',
                                        code='tipo_ou_marca_inativo')
            
        return data
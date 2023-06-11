from django import forms
from django.forms import ModelForm
from app.models import Modelos, Tipos, Marcas

class ModeloForm(ModelForm):
    fk_tipo = forms.ModelChoiceField(queryset=Tipos.objects.filter(fk_status__descricao = 'Ativo'), label = 'Tipo de veiculo')
    fk_marca = forms.ModelChoiceField(queryset=Marcas.objects.filter(fk_status__descricao = 'Ativo'), label = 'Marca')
    
    class Meta:
        model = Modelos
        fields = ['descricao', 'fk_tipo', 'fk_marca']

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
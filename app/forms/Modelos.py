from django import forms
from django.forms import ModelForm
from app.models import Modelos, Tipos

class ModeloForm(ModelForm):
    fk_tipo = forms.ModelChoiceField(queryset=Tipos.objects.filter(fk_status__descricao = 'Ativo'))
    
    class Meta:
        model = Modelos
        fields = ['descricao', 'fk_tipo']

class StatusModeloForm(ModelForm):
    
    class Meta:
        model = Modelos
        fields = ['fk_status']
    
    def clean(self) -> dict[str, any]:
        data = super().clean()
        status_set = data.get("fk_status").descricao
        status_tipo = self.instance.fk_tipo.fk_status.descricao
        
        if status_set == 'Ativo' and status_tipo == 'Inativo':
            raise forms.ValidationError('Não é possível ativar um modelo de veiculo com tipo inativado, primeiro ative novamente tipo de veiculo.',
                                        code='tipo_inativo')
            
        return data
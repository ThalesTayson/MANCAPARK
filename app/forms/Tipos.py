from django import forms
from django.forms import Form, ModelForm
from app.models import Modelos, Marcas, Status, Tipos

class TipoForm(ModelForm):
    fk_marca = forms.ModelChoiceField(queryset=Marcas.objects.filter(fk_status__descricao = 'Ativo'))
    
    class Meta:
        model = Tipos
        fields = ['descricao', 'fk_marca']

class StatusTipoForm(ModelForm):
    
    class Meta:
        model = Tipos
        fields = ['fk_status']
        
    def clean(self) -> dict[str, any]:
        data = super().clean()
        status_set = data.get("fk_status").descricao
        status_marca = self.instance.fk_marca.fk_status.descricao
        
        if status_set == 'Ativo' and status_marca == 'Inativo':
            raise forms.ValidationError('Não é possível ativar um tipo de veiculo com marca inativada, primeiro ative novamente a marca.',
                                        code='marca_inativa')
            
        return data

    def save(self):
        data = super().save(True)
        
        if data.fk_status.descricao == 'Inativo':
            for modelo in Modelos.objects.filter(fk_tipo = data):
                modelo.fk_status = self.cleaned_data['fk_status']
                modelo.save()
        
        return data
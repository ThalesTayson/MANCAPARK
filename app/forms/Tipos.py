from django.forms import ModelForm
from app.models import Modelos, Tipos

class TipoForm(ModelForm):
    
    class Meta:
        model = Tipos
        fields = ['descricao']

class StatusTipoForm(ModelForm):
    
    class Meta:
        model = Tipos
        fields = ['fk_status']

    def save(self):
        data = super().save(True)
        
        if data.fk_status.descricao == 'Inativo':
            for modelo in Modelos.objects.filter(fk_tipo = data):
                modelo.fk_status = self.cleaned_data['fk_status']
                modelo.save()
        
        return data
from django.forms import ModelForm
from app.models import Modelos, Marcas, Tipos

class MarcaForm(ModelForm):
    class Meta:
        model = Marcas
        fields = ['descricao']

class StatusMarcaForm(ModelForm):
    
    class Meta:
        model = Marcas
        fields = ['fk_status']
    
    def save(self):
        data = super().save(True)
        
        if data.fk_status.descricao == 'Inativo':
            for tipo in Tipos.objects.filter(fk_marca = data):
                tipo.fk_status = self.cleaned_data['fk_status']
                tipo.save()
                
                for modelo in Modelos.objects.filter(fk_tipo = tipo):
                    modelo.fk_status = self.cleaned_data['fk_status']
                    modelo.save()
        
        return data
    
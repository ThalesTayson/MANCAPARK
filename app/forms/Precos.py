from django.forms import ModelForm
from app.models import Precos, Status

class PrecoForm(ModelForm):
    class Meta:
        model = Precos
        fields = ['fk_tipo', 'por_mensalidade', 'por_hora']
    
    def save(self):
        data = super().save(False)

        try: lastpreco = Precos.objects.get(fk_tipo = self.cleaned_data['fk_tipo'], fk_status__descricao = 'Ativo')
        except: lastpreco = None

        if lastpreco is not None:
            lastpreco.fk_status = Status.objects.get(descricao = 'Inativo')
            lastpreco.save()
            
        data.save()
        
        return data
    
from django.forms import ModelForm
from app.models import Clientes

class ClienteForm(ModelForm):
    class Meta:
        model = Clientes
        fields = ['primeiro_nome', 'ultimo_nome', 'email', 'telefone']
from django import forms
from django.forms import Form, ModelForm
from app.models import Veiculos, Modelos, Marcas, Status

class VeiculoForm(ModelForm):
    class Meta:
        model = Veiculos
        fields = ['placa', 'fk_modelo', 'fk_cliente']

class StatusVeiculoForm(Form):
    fk_status = forms.ModelChoiceField(queryset=Status.objects)
    fk_veiculo = forms.ModelChoiceField(queryset=Veiculos.objects)
    
    def save(self):
        veiculo = self.cleaned_data['fk_veiculo']
        veiculo.fk_status = self.cleaned_data['fk_status']
        return veiculo.save(True)
        
class ModeloForm(ModelForm):
    class Meta:
        model = Modelos
        fields = ['descricao', 'fk_marca']

class StatusModeloForm(Form):
    fk_status = forms.ModelChoiceField(queryset=Status.objects)
    fk_modelo = forms.ModelChoiceField(queryset=Modelos.objects)
    
    def save(self):
        modelo = self.cleaned_data['fk_modelo']
        modelo.fk_status = self.cleaned_data['fk_status']
        return modelo.save(True)
    
class MarcaForm(ModelForm):
    class Meta:
        model = Marcas
        fields = ['descricao']

class StatusMarcaForm(Form):
    fk_status = forms.ModelChoiceField(queryset=Status.objects)
    fk_marca = forms.ModelChoiceField(queryset=Marcas.objects)
    
    def save(self):
        marca = self.cleaned_data['fk_marca']
        marca.fk_status = self.cleaned_data['fk_status']
        return marca.save(True)
    
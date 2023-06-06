from django import forms
from django.forms import Form, ModelForm
from app.models import Veiculos, Modelos, Marcas, Status, Clientes

class VeiculoForm(ModelForm):
    fk_modelo = forms.ModelChoiceField(queryset=Modelos.objects.filter(fk_status__descricao = 'Ativo'))
    fk_cliente = forms.ModelChoiceField(queryset=Clientes.objects.filter(fk_status__descricao = 'Ativo'))
    
    class Meta:
        model = Veiculos
        fields = ['placa', 'fk_modelo', 'fk_cliente']

class StatusVeiculoForm(Form):
    fk_status = forms.ModelChoiceField(queryset=Status.objects)
    fk_veiculo = forms.ModelChoiceField(queryset=Veiculos.objects)
    
    def clean(self) -> dict[str, any]:
        data = super().clean()
        status_set = data.get("fk_status").descricao
        status_cliente = data.get("fk_veiculo").fk_cliente.fk_status.descricao
        
        if status_set == 'Ativo' and status_cliente == 'Inativo'> 0:
            raise forms.ValidationError('Não é possível ativar um veiculo de cliente inativado, primeiro ative novamente o cliente.',
                                        code='marca_inativa')
            
        return data
    
    def save(self):
        veiculo = self.cleaned_data['fk_veiculo']
        veiculo.fk_status = self.cleaned_data['fk_status']
        veiculo.save()
        return veiculo
        
class ModeloForm(ModelForm):
    fk_marca = forms.ModelChoiceField(queryset=Marcas.objects.filter(fk_status__descricao = 'Ativo'))
    
    class Meta:
        model = Modelos
        fields = ['descricao', 'fk_marca']

class StatusModeloForm(Form):
    fk_status = forms.ModelChoiceField(queryset=Status.objects)
    fk_modelo = forms.ModelChoiceField(queryset=Modelos.objects)
    
    def clean(self) -> dict[str, any]:
        data = super().clean()
        status_set = data.get("fk_status").descricao
        status_marca = data.get("fk_modelo").fk_marca.fk_status.descricao
        
        if status_set == 'Ativo' and status_marca == 'Inativo'> 0:
            raise forms.ValidationError('Não é possível ativar um modelo de veiculo com marca inativada, primeiro ative novamente a marca.',
                                        code='marca_inativa')
            
        return data
    
    def save(self):
        modelo = self.cleaned_data['fk_modelo']
        modelo.fk_status = self.cleaned_data['fk_status']
        modelo.save()
        return modelo
    
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
        
        marca.save()
        
        if marca.fk_status.descricao == 'Inativo':
            for modelo in Modelos.objects.filter(fk_marca = marca):
                modelo.fk_status = self.cleaned_data['fk_status']
                modelo.save()
        
        return marca
    
from django import forms
from django.forms import ModelForm
from app.models import TiposRegistros ,Registros, Estacionamento, Veiculos, Status, Pagamentos, Precos, Avulsos
from app.tools import calculaTempo
from django.utils import timezone

class EntradaForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(EntradaForm, self).__init__(*args, **kwargs)
        
        rawSQL = Veiculos.objects.raw(
            "SELECT v.id as id FROM app_veiculos v " +
            "LEFT JOIN app_estacionamento e ON e.fk_veiculo_id = v.id " +
            "WHERE e.fk_status_id = 2 OR e.id IS NULL;"
        )
        self.fields['fk_veiculo'].queryset = Veiculos.objects.filter(id__in = [q.id for q in rawSQL])
    
    class Meta:
        model = Registros
        fields = ['fk_veiculo']
    
    def clean(self) -> dict[str, any]:
        data = super().clean()
        veiculo = data.get("fk_veiculo")
        ests = Estacionamento.objects.filter(fk_veiculo = veiculo)
        
        if len(ests) > 0:
            if ests[0].fk_status.descricao == 'Ativo':
                raise forms.ValidationError('Veiculo já se encontra no Estacionamento!',
                                        code='veiculo_ativo_no_estacionamento')
        
        return data
        
    def save(self, user):
        data =  super().save(False)
        data.fk_tipoRegistro = TiposRegistros.objects.get(descricao = "Entrada")
        data.fk_usuario = user
        
        status = Status.objects.get(
            descricao = 'Ativo'
        )
        
        data.fk_status = status
        
        try:
            est = Estacionamento.objects.get(fk_veiculo=data.fk_veiculo)
        except:
            est = Estacionamento()
            est.fk_veiculo = data.fk_veiculo
        
        est.fk_status = status
                
        est.save()
        data.save()
        
        return data
    
class SaidaForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(SaidaForm, self).__init__(*args, **kwargs)
        
        rawSQL = Veiculos.objects.raw(
            "SELECT v.id as id FROM app_veiculos v " +
            "INNER JOIN app_estacionamento e ON e.fk_veiculo_id = v.id " +
            "WHERE e.fk_status_id = 1;"
        )
        self.fields['fk_veiculo'].queryset = Veiculos.objects.filter(id__in = [q.id for q in rawSQL])
        
    class Meta:
        model = Registros
        fields = ['fk_veiculo']
    
    def clean(self) -> dict[str, any]:
        data = super().clean()
        veiculo = data.get("fk_veiculo")
        ests = Estacionamento.objects.filter(fk_veiculo = veiculo)
        
        if len(ests) > 0:
            if ests[0].fk_status.descricao == 'Inativo':
                raise forms.ValidationError('Veiculo já saiu do Estacionamento!',
                                        code='veiculo_inativo_no_estacionamento')
        
        return data

    def getValor(self):
        data =  super().save(False)
        
        reg_entrada = Registros.objects.get(
            fk_veiculo = data.fk_veiculo,
            fk_tipoRegistro__descricao = 'Entrada', 
            fk_status__descricao = 'Ativo'
        )
            
            
        if data.fk_veiculo.fk_status.descricao == 'Ativo':
            return None, reg_entrada, 0
        else:
            
            preco = Precos.objects.get(
                    fk_status__descricao = 'Ativo', 
                    fk_tipo = data.fk_veiculo.fk_modelo.fk_tipo
                )
            
            tempo = calculaTempo(reg_entrada.created_at, timezone.now())
            
            return preco, reg_entrada, (preco.por_hora * tempo)
        
    def save(self, user):
        data =  super().save(False)
        data.fk_tipoRegistro = TiposRegistros.objects.get(descricao = "Saida")
        data.fk_usuario = user

        pag = Pagamentos() if data.fk_veiculo.fk_status.descricao == 'Inativo' else None
        avulso = Avulsos() if data.fk_veiculo.fk_status.descricao == 'Inativo' else None
        
        status = Status.objects.get(
            descricao = 'Inativo'
        )
        
        data.fk_status = status
        
        try:
            est = Estacionamento.objects.get(fk_veiculo=data.fk_veiculo)
        except:
            est = Estacionamento()
            est.fk_veiculo = data.fk_veiculo
        
        est.fk_status = status
        
        preco, reg_entrada, valor = self.getValor()
        
        reg_entrada.fk_status = status
            
        reg_entrada.save()
        
        if pag is not None:
            
            avulso.fk_registro_entrada = reg_entrada
            
            pag.valor = valor
            pag.save()
            pag.fk_preco.add(preco)
                
        est.save()
        data.save()
        if avulso is not None:
            avulso.fk_registro_saida = data
            avulso.pagamento = pag
            avulso.save()
        
        return data
        
    
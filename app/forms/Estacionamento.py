from django import forms
from django.forms import ModelForm
from app.models import Registros, Estacionamento, Veiculos, Status, Pagamentos, Precos, Avulsos
from app.tools import calculaTempo
from django.utils import timezone

class EstacionamentoForm(ModelForm):
    
    fk_veiculo = forms.ModelChoiceField(queryset=Veiculos.objects, label= 'Veiculo')
    
    class Meta:
        model = Registros
        fields = ['fk_tipoRegistro', 'fk_veiculo']
    
    def clean(self) -> dict[str, any]:
        data = super().clean()
        tp_reg = data.get("fk_tipoRegistro")
        veiculo = data.get("fk_veiculo")
        ests = Estacionamento.objects.filter(fk_veiculo = veiculo)
        
        if len(ests) > 0:
            if ests[0].fk_status.descricao == 'Ativo' and tp_reg.descricao == 'Entrada':
                raise forms.ValidationError('Veiculo já se encontra no Estacionamento!',
                                        code='veiculo_ativo_no_estacionamento')
            if ests[0].fk_status.descricao == 'Inativo' and tp_reg.descricao == 'Saida':
                raise forms.ValidationError('Veiculo já saiu do Estacionamento!',
                                        code='veiculo_inativo_no_estacionamento')
        
        return data

    def getValor(self):
        data =  super().save(False)
        tp_reg = data.fk_tipoRegistro.descricao
        
        reg_entrada = None
        if tp_reg == 'Saida':
            reg_entrada = Registros.objects.get(
                fk_veiculo = data.fk_veiculo,
                fk_tipoRegistro__descricao = 'Entrada', 
                fk_status__descricao = 'Ativo'
            )
            
        if tp_reg == 'Entrada' or data.fk_veiculo.fk_status == 'Ativo':
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
        data.fk_usuario = user
        tp_reg = data.fk_tipoRegistro.descricao

        pag = Pagamentos() if data.fk_veiculo.fk_status.descricao == 'Inativo' and tp_reg == 'Saida' else None
        avulso = Avulsos() if data.fk_veiculo.fk_status.descricao == 'Inativo' and tp_reg == 'Saida' else None
        
        status = Status.objects.get(
            descricao = 'Ativo' if tp_reg == 'Entrada' else 'Inativo'
        )
        
        data.fk_status = status
        
        try:
            est = Estacionamento.objects.get(fk_veiculo=data.fk_veiculo)
        except:
            est = Estacionamento()
            est.fk_veiculo = data.fk_veiculo
        
        est.fk_status = status
        
        if tp_reg == 'Saida':
            preco, reg_entrada, valor = self.getValor()
            print(valor)
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
        
    
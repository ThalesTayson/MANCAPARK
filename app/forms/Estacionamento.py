from django import forms
from django.forms import ModelForm
from app.models import Registros, Estacionamento, Veiculos, Status, Pagamentos, Precos, Avulsos
from app.tools import calculaTempo

class EstacionamentoForm(ModelForm):
    fk_veiculo = forms.ModelChoiceField(queryset=Veiculos.objects.filter(fk_status__descricao = 'Ativo'))
    
    class Meta:
        model = Registros
        fields = ['fk_tipoRegistro', 'fk_veiculo', 'fk_usuario']
    
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
                
    def save(self):
        data =  super().save(False)
        tp_reg = data.fk_tipoRegistro.descricao

        pag = Pagamentos() if data.fk_veiculo.fk_status == 'Inativo' and tp_reg == 'Saida' else None
        avulso = Avulsos() if data.fk_veiculo.fk_status == 'Inativo' and tp_reg == 'Saida' else None
        
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
            
            reg_entrada = Registros.objects.get(fk_tipoRegistro__descricao = 'Entrada', fk_status__descricao = 'Ativo')
            reg_entrada.fk_status = status
            reg_entrada.save()
            
            if pag is not None:
                avulso.fk_registro_entrada = reg_entrada
                tempo = calculaTempo(reg_entrada.created_at, data.created_at)
                preco = Precos.objects.get(
                    fk_status__descricao = 'Ativo', 
                    fk_tipo = data.fk_veiculo.fk_modelo.fk_tipo
                )
                pag.valor = preco.por_hora * tempo
                pag.fk_preco.add(preco)
                pag.save()
                
        est.save()
        data.save()
        if avulso is not None:
            avulso.fk_registro_saida = data
            avulso.pagamento = pag
            avulso.save()
        
        return data
        
    
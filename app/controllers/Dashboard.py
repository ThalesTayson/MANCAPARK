from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils import timezone
from django.db.models import Count, Sum, DateField
from django.db.models.functions import Cast

from app.models import Estacionamento, Registros, Precos, Pagamentos
from app.tools import calculaTempo, local_to_utc

@login_required
def dados(req):
    now = timezone.now().replace(hour=0,minute=0,second=0,microsecond=0)
    total_estacionados = Estacionamento.objects.filter(fk_status__descricao = 'Ativo').count()
    total_de_entradas = Registros.objects.filter(
        created_at__gte = now, 
        fk_tipoRegistro__descricao = 'Entrada'
    ).count()
    
    valor = 0
    query = Estacionamento.objects.filter(
        fk_status__descricao = 'Ativo', 
        fk_veiculo__fk_status__descricao = 'Inativo'
    )
    for row in query:
        reg_entrada = Registros.objects.get(
            fk_veiculo = row.fk_veiculo,
            fk_tipoRegistro__descricao = 'Entrada', 
            fk_status__descricao = 'Ativo'
        )
        tempo = calculaTempo(reg_entrada.created_at, timezone.now())
        preco = Precos.objects.get(
                fk_status__descricao = 'Ativo', 
                fk_tipo = row.fk_veiculo.fk_modelo.fk_tipo
        )
        valor += float(preco.por_hora * tempo)
    total_a_receber = str("R$ %.2f" % float(valor)).replace('.', ',')
    
    valor = 0
    query = Pagamentos.objects.filter(created_at__gte = now)
    for row in query: valor += float(row.valor)
    total_recebidos_do_dia = str("R$ %.2f" % float(valor)).replace('.', ',')
    
    totais_por_tipo = []
    query = Registros.objects.filter(
        created_at__gte = (now - timezone.timedelta(days=30)),
        fk_tipoRegistro__descricao = 'Entrada'
    ).values(
        'fk_veiculo__fk_modelo__fk_tipo__descricao'
    ).annotate(count=Count('fk_veiculo__fk_modelo__fk_tipo__id')
    ).order_by(
        'fk_veiculo__fk_modelo__fk_tipo__descricao'
    )
    for row in query: 
        totais_por_tipo.append([
            row.get('fk_veiculo__fk_modelo__fk_tipo__descricao'),
            row.get('count')
        ])
    
    data = {
        "total_estacionados": total_estacionados,
        "total_de_entradas": total_de_entradas,
        "total_a_receber": total_a_receber,
        "total_recebidos_do_dia": total_recebidos_do_dia,
        "totais_de_entradas_por_tipo_ultimo_mes": totais_por_tipo
    }
        
    return JsonResponse(data={"data":data})

def graficoFaturamento(req):
    now = timezone.now().replace(hour=0,minute=0,second=0,microsecond=0)
    try: 
        date_ini = local_to_utc(timezone.datetime.strptime(req.GET['date_inicial'], '%Y-%m-%d'))
        date_fim = local_to_utc(timezone.datetime.strptime(req.GET['date_fim'], '%Y-%m-%d')) + timezone.timedelta(days=1)
    except:
        date_ini = (now - timezone.timedelta(days=7))
        date_fim = (now + timezone.timedelta(days=1))
        
    data = []
    
    query = Pagamentos.objects.filter(
        created_at__gte = date_ini,
        created_at__lte = date_fim
    ).values(date=Cast('created_at', DateField())).annotate(valor=Sum('valor')
    ).order_by('date')
    
    for row in query: 
        _date = row.get('date').strftime("%d/%m")
        _valor = float(row.get('valor'))
        
        data.append({"DATA": _date, "VALOR": _valor})
    
    return JsonResponse(data={"data":data})     

def graficoEntradas(req):
    now = timezone.now().replace(hour=0,minute=0,second=0,microsecond=0)
    try: 
        date_ini = local_to_utc(timezone.datetime.strptime(req.GET['date_inicial'], '%Y-%m-%d'))
        date_fim = local_to_utc(timezone.datetime.strptime(req.GET['date_fim'], '%Y-%m-%d')) + timezone.timedelta(days=1)
    except:
        date_ini = (now - timezone.timedelta(days=7))
        date_fim = (now + timezone.timedelta(days=1))
    
    query = Registros.objects.filter(
        created_at__gte = date_ini,
        created_at__lte = date_fim,
        fk_tipoRegistro__descricao = 'Entrada'
    ).values(date=Cast('created_at', DateField())).annotate(count=Count('id')
    ).order_by('date')
    
    data = []
    for row in query: 
        _date = row.get('date').strftime("%d/%m")
        _valor = int(row.get('count'))
        
        data.append({"DATA": _date, "TOTAL": _valor})
    
    return JsonResponse(data={"data":data})
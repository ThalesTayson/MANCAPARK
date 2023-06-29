from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils import timezone
from django.db.models import Count, Sum, DateField
from django.db.models.functions import Cast

from app.models import Estacionamento, Registros, Precos, Pagamentos, Avulsos
from app.tools import calculaTempo, local_to_utc

@login_required
def dados(req):
    
    # Comparation dates
    now = timezone.now().replace(hour=0,minute=0,second=0,microsecond=0)
    yesterday = timezone.now() - timezone.timedelta(days=1)
    thirty_days = now - timezone.timedelta(days=30)
    
    last_24_hours = Registros.objects.filter(
            fk_tipoRegistro__descricao = 'Entrada', 
            fk_status__descricao = 'Inativo', 
            created_at__gte =  yesterday,
            created_at__lte =  now - timezone.timedelta(minutes=60)).count()
    parked_total_now = Estacionamento.objects.filter(fk_status__descricao = 'Ativo').count()
    try: parked_indexes = (parked_total_now * 100) / last_24_hours
    except: parked_indexes = 100
    parked = {
        'title': 'Estacionados',
        "total": parked_total_now,
        "indexes": parked_indexes - (last_24_hours / 24),
        'subtitle': 'em relação às ultimas 24 horas.'
    }
    
    last_30_days = Registros.objects.filter(
            fk_tipoRegistro__descricao = 'Entrada', 
            fk_status__descricao = 'Inativo', created_at__gte =  thirty_days).count()
    entrances_total_today = Registros.objects.filter(
            created_at__gte = now, 
            fk_tipoRegistro__descricao = 'Entrada').count()
    try: entrances_indexes = (entrances_total_today * 100) / last_30_days
    except: entrances_indexes = 100
    entrances = {
        'title': 'Total de Entradas Hoje',
        "total": entrances_total_today,
        "indexes": entrances_indexes - (last_30_days / 30),
        'subtitle': 'em relação aos ultimos 30 dias.'
    }
    
    payment_receive = 0
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
        payment_receive += float(preco.por_hora * tempo)
    query = Avulsos.objects.filter(
        pagamento__created_at__gte = yesterday
    ).aggregate(total=Sum('pagamento__valor'))
    
    payment_last_24_hours = float(query.get('total')) if query.get('total') is not None else 0.0
    try: payments_indexes = (payment_receive * 100) / payment_last_24_hours
    except: payments_indexes = 100
    payments_receive = {
        'title': 'Total a Receber',
        'total': str("R$ %.2f" % float(payment_receive)).replace('.', ','),
        'indexes': payments_indexes - (payment_last_24_hours / 24),
        'subtitle': 'em relação às ultimas 24 horas.'
    }
    
    payments_total_today = 0
    query = Pagamentos.objects.filter(created_at__gte = now)
    for row in query: payments_total_today += float(row.valor)
    query = Pagamentos.objects.filter(
        created_at__gte = thirty_days,
        created_at__lte = now
    ).aggregate(total=Sum('valor'))
    payments_last_30_days = float(query.get('total')) if query.get('total') is not None else 0.0
    try: payments_indexes = (payments_total_today * 100) / payments_last_30_days
    except: payments_indexes = 100
    
    payments_received = {
        'title': 'Total Recebido',
        'total': str("R$ %.2f" % float(payments_total_today)).replace('.', ','),
        'indexes': payments_indexes - (payments_last_30_days / 30),
        'subtitle': 'em relação aos ultimos 30 dias.'
    }
    
    data = {
        "parked": parked,
        "entrances": entrances,
        "payments_receive": payments_receive,
        "payments_received": payments_received
    }
        
    return JsonResponse(data={"data":data})

def graficoTipos(req):
    now = timezone.now().replace(hour=0,minute=0,second=0,microsecond=0)
    thirty_days = now - timezone.timedelta(days=30)
    
    type_last_month = []
    
    query = Registros.objects.filter(
        created_at__gte = (thirty_days - timezone.timedelta(days=30)),
        fk_tipoRegistro__descricao = 'Entrada'
    ).values(
        'fk_veiculo__fk_modelo__fk_tipo__descricao'
    ).annotate(count=Count('fk_veiculo__fk_modelo__fk_tipo__id')
    ).order_by(
        'fk_veiculo__fk_modelo__fk_tipo__descricao'
    )
    
    for row in query: 
        type_last_month.append({
            "key": row.get('fk_veiculo__fk_modelo__fk_tipo__descricao'),
            "value": row.get('count')
        })
    
    return JsonResponse(data={"data":type_last_month})

def graficoFaturamento(req):
    now = timezone.now().replace(hour=0,minute=0,second=0,microsecond=0)
    try: 
        date_ini = local_to_utc(timezone.datetime.strptime(req.GET['date_inicial'], '%Y-%m-%d'))
        date_fim = local_to_utc(timezone.datetime.strptime(req.GET['date_fim'], '%Y-%m-%d')) + timezone.timedelta(days=1)
    except:
        date_ini = (now - timezone.timedelta(days=30))
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
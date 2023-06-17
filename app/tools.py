import re
from datetime import timezone

def utc_to_local(utc_dt):
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)

def local_to_utc(dt):
    return dt.replace(tzinfo=None).astimezone(tz=timezone.utc)

def formToJson(form):
    data = []
    fields = form.fields.keys()
    errors = form.errors
    
    for field in fields:
        obj_field = form.fields.get(field)
        d = {"id": field}
        
        d.setdefault('input_type', obj_field.widget.input_type)
        d.setdefault('label', obj_field.label)
        d.setdefault('is_hidden', obj_field.widget.is_hidden)
        d.setdefault('is_required', obj_field.widget.is_required)
        d.setdefault('attrs', obj_field.widget.attrs)
        
        try:
            d.setdefault('value', str(form.instance.__getattribute__(field)))
        except: d.setdefault('value', '')
        
        try:
            d.setdefault('error', str(errors.get(field).as_text()))
        except: d.setdefault('error', "")
        
        if d['input_type'] == 'select':
            d.setdefault('is_multiple', obj_field.widget.allow_multiple_selected)
            
            choices = {}
            for choice in obj_field.queryset:
                choices.setdefault(choice.pk, str(choice))
                
            d.setdefault('options', choices)
        
        data.append(d)
        
    return data

def calculaTempo(entrada, saida):
    tempo = ((saida - entrada).seconds / 3600) # transforma timedelta em horas
    if int(tempo) == 0:
        tempo = 1 if (tempo * 60) > 15 and (tempo * 60) < 60 else 0 #Primeiros 15 min não paga
    else:
        tempo = int(tempo) + 1 if tempo > int(tempo) else int(tempo) #Após 1h apartir dos 1s a mais paga a próxima hora completa.
    
    return tempo

def calculaTempo_em_hour_e_min(entrada, saida):
    min = int((saida - entrada).seconds / 60)
    hour = int(min / 60)
    min = min - (hour * 60)
    
    return "{}h e {}m".format(hour, min)

def maskTelefone(telefone):
    return re.sub(r'(\d{2})(\d{1})(\d{8})', r'(\1) \2 \3', str(telefone))
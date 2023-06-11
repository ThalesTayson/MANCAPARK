import re
from datetime import timezone

def utc_to_local(utc_dt):
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)

def formToJson(form):
    data = {}
    fields = form.fields.keys()
    for field in fields:
        obj_field = form.base_fields.get(field)
        data.setdefault(field, {})
        data[field].setdefault('input_type', obj_field.widget.input_type)
        data[field].setdefault('label', obj_field.label)
        data[field].setdefault('is_hidden', obj_field.widget.is_hidden)
        data[field].setdefault('is_required', obj_field.widget.is_required)
        data[field].setdefault('attrs', obj_field.widget.attrs)
        
        if data[field]['input_type'] == 'select':
            data[field].setdefault('multiple', obj_field.widget.allow_multiple_selected)
            
            choices = []
            for choice in obj_field.choices.queryset:
                choices.append({'value': choice.pk, 'text': str(choice) })
                
            data[field].setdefault('options', choices)
            
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
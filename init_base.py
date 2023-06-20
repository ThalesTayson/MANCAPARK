import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mancapark.settings')
django.setup()

from app.models import Status, TiposRegistros, Usuarios

if Status.objects.filter().count() == 0 :
    if TiposRegistros.objects.filter().count() == 0:
        if Usuarios.objects.filter().count() == 0:

            status = Status() 
            status.descricao = 'Ativo'
            status.save()
            status = Status()
            status.descricao = 'Inativo' 
            status.save()     
            tp_reg = TiposRegistros() 
            tp_reg.descricao = 'Entrada'
            tp_reg.save()                
            tp_reg = TiposRegistros()    
            tp_reg.descricao = 'Saida'   
            tp_reg.save()              
            user = Usuarios()          
            user.username = 'Usuario1'
            user.password = 'senh@123' 
            user.username = 'usuario1' 
            user.email = 'usuario1@1.com' 
            user.first_name = 'Usuario'
            user.last_name = 'Um' 
            user.set_password('senh@123') 
            user.save()
            user = Usuarios()             
            user.username = 'Usuario1'
            user.username = 'usuario2' 
            user.email = 'usuario2@2.com' 
            user.first_name = 'Usuario'   
            user.last_name = 'Dois'       
            user.set_password('senh@321') 
            user.save()
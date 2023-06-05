from django.db import models
from django.contrib.auth.models import AbstractUser

"""
TABELAS 

status (id, descricao, created_at, updated_at)
usuarios (id, username, password, email, first_name, last_name, fk_status, created_at, updated_at)
clientes (id, primeiro_nome, ultimo_nome, email, telefone, fk_status, created_at, updated_at)
marcas (id, descricao, fk_status, created_at, updated_at)
modelos (id, descricao, fk_marca, fk_status, created_at, updated_at)
veiculos (id, placa, fk_cliente, fk_modelo, fk_status, created_at, updated_at)
tiposRegistro (id, descricao, fk_status, created_at, updated_at)
registros (id, fk_veiculo, fk_usuario, fk_tipoRegistro, created_at, updated_at)
estacionamento (id, fk_veiculos, fk_status, created_at, updated_at)

"""
class Status ( models.Model ): # Ativo/Inativo
    descricao = models.CharField(max_length=15, unique = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
class Usuarios ( AbstractUser ):
    # herdará username
    # herdará password
    # herdará email
    # herdará first_name
    # herdará last_name
    fk_status = models.ForeignKey(Status, on_delete = models.CASCADE, default=1)
    is_staff = models.BooleanField(default = False) #Tira o Acesso do Django Admin
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self) -> str:
        return self.first_name

class Clientes ( models.Model ):
    primeiro_nome = models.CharField(max_length = 50)
    ultimo_nome = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 70, unique = True)
    telefone = models.BigIntegerField(unique = True)
    fk_status = models.ForeignKey(Status, on_delete = models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
class Marcas ( models.Model ):
    descricao = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Modelos ( models.Model ):
    descricao = models.CharField(max_length = 50)
    fk_marca = models.ForeignKey(Marcas, on_delete = models.CASCADE)
    fk_status = models.ForeignKey(Status, on_delete = models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
class Veiculos ( models.Model ):
    placa = models.CharField(max_length = 50, unique = True)
    fk_modelo = models.ForeignKey(Modelos, on_delete = models.CASCADE)
    fk_cliente = models.ForeignKey(Clientes, on_delete = models.CASCADE)
    fk_status = models.ForeignKey(Status, on_delete = models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class TiposRegistro ( models.Model ): # Entrada/Saida
    descricao = models.CharField(max_length=15, unique = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
class Registros ( models.Model ):
    fk_tipoRegistro = models.ForeignKey(TiposRegistro, on_delete = models.CASCADE)
    fk_veiculo = models.ForeignKey(Veiculos, on_delete = models.CASCADE)
    fk_usuario = models.ForeignKey(Usuarios, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Estacionamento ( models.Model ):
    fk_veiculo = models.ForeignKey(Veiculos, on_delete = models.CASCADE)
    fk_status = models.ForeignKey(Status, on_delete = models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
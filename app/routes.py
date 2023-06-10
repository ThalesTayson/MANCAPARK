from django.urls import path
from .controllers import Templates, Clientes, Estacionamento, Marcas, Mensalidades, Modelos, Tipos,Veiculos, Precos

urlpatterns = [
    
    path('', Templates.home, name='home'),
    
    path('clientes/create', Clientes.create, name='createCliente'),
    path('clientes/<int:id>/update', Clientes.update, name='updateCliente'),
    
    path('marcas/create', Marcas.create, name='createMarca'),
    path('marcas/<int:id>/update', Marcas.update, name='updateMarca'),
    path('marcas/<int:id>/status/update', Marcas.status_update, name='updateStatusMarca'),
    
    path('modelos/create', Modelos.create, name='createModelo'),
    path('modelos/<int:id>/update', Modelos.update, name='updateModelo'),
    path('modelos/<int:id>/status/update', Modelos.status_update, name='updateStatusModelo'),

    path('tipos/create', Tipos.create, name='createTipo'),
    path('tipos/<int:id>/update', Tipos.update, name='updateTipo'),
    path('tipos/<int:id>/status/update', Tipos.status_update, name='updateStatusTipo'),

    path('veiculos/create', Veiculos.create, name='createVeiculo'),
    path('veiculos/<int:id>/update', Veiculos.update, name='updateVeiculo'),
    path('veiculos/<int:id>/status/update', Veiculos.status_update, name='updateStatusVeiculo'),
    
    path('precos/create', Precos.create, name='createPreco'),
    
    path('mensalidades/create', Mensalidades.create, name='createMensalidade'),
    path('mensalidades/cliente/<int:id>/inativar', Mensalidades.cliente_inativar, name='inativarMensalidade'),
    
    path('estacionamento/lancar-registro', Estacionamento.update, name='lancarRegistro'),
]

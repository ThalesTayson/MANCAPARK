from django.urls import path
from .controllers import Templates, Clientes, Estacionamento, Marcas, Mensalidades, Modelos, Tipos,Veiculos, Precos, Dashboard

urlpatterns = [
    
    path('', Templates.home, name='home'),
    
    path('clientes/create', Clientes.create, name='createCliente'),
    path('clientes/<int:id>/update', Clientes.update, name='updateCliente'),
    path('clientes/lista', Clientes.lista, name='listaClientes'),
    
    path('marcas/create', Marcas.create, name='createMarca'),
    path('marcas/<int:id>/update', Marcas.update, name='updateMarca'),
    path('marcas/<int:id>/status/update', Marcas.status_update, name='updateStatusMarca'),
    path('marcas/lista', Marcas.lista, name='listaMarcas'),
    
    path('modelos/create', Modelos.create, name='createModelo'),
    path('modelos/<int:id>/update', Modelos.update, name='updateModelo'),
    path('modelos/<int:id>/status/update', Modelos.status_update, name='updateStatusModelo'),
    path('modelos/lista', Modelos.lista, name='listaModelos'),
    
    path('tipos/create', Tipos.create, name='createTipo'),
    path('tipos/<int:id>/update', Tipos.update, name='updateTipo'),
    path('tipos/<int:id>/status/update', Tipos.status_update, name='updateStatusTipo'),
    path('tipos/lista', Tipos.lista, name='listaTipos'),
    
    path('veiculos/create', Veiculos.create, name='createVeiculo'),
    path('veiculos/<int:id>/update', Veiculos.update, name='updateVeiculo'),
    path('veiculos/<int:id>/status/update', Veiculos.status_update, name='updateStatusVeiculo'),
    path('veiculos/lista', Veiculos.lista, name='listaVeiculos'),
    
    path('precos/create', Precos.create, name='createPreco'),
    path('precos/lista', Precos.lista, name='listaPrecos'),
    
    path('mensalidades/create', Mensalidades.create, name='createMensalidade'),
    path('mensalidades/cliente/<int:id>/inativar', Mensalidades.cliente_inativar, name='inativarMensalidade'),
    path('mensalidades/lista', Mensalidades.lista, name='listaMensalidades'),
    
    path('estacionamento/lancar-entrada', Estacionamento.entrada, name='lancarEntrada'),
    path('estacionamento/lancar-saida', Estacionamento.saida, name='lancarSaida'),
    path('estacionamento/lista', Estacionamento.lista, name='listaMEstacionamento'),
    
    path('dashboard/dados', Dashboard.dados, name='dados'),
    path('dashboard/grafico-entradas', Dashboard.graficoEntradas, name='grafico'),
    path('dashboard/grafico-faturamento', Dashboard.graficoFaturamento, name='grafico'),
    
]

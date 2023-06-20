from django.urls import include
from django.urls import path
from app.controllers.Templates import entrar, sair

urlpatterns = [
    path('', include('app.routes'), name = 'app'),
    path('accounts/auth/login', entrar, name = 'login'),
    path('accounts/auth/logout', sair, name = 'logout'),
]

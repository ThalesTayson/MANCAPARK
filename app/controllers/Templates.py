from django.shortcuts import render, redirect
from app.forms.Auth import formAuthenticate
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from app.forms.Clientes import ClienteForm

def entrar(req):
    
    form = formAuthenticate()
    
    if ( req.POST ):
        form = formAuthenticate(req.POST, req.FILES)
        if form.is_valid():
            user = form.login()
            login(req, user)
            return redirect('home')
            
    return render(req,'login.html', {"form":form})

@login_required
def sair(req):
    logout(req)
    return redirect('login')

@login_required
def home(req):
    
    return render(req,'index.html')
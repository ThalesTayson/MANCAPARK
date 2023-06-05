from django.shortcuts import render, redirect
from .forms.Auth import formAuthenticate
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

def loginn(req):
    
    form = formAuthenticate()
    
    if ( req.POST ):
        form = formAuthenticate(req.POST, req.FILES)
        if form.is_valid():
            user = form.login()
            login(req, user)
            return redirect('home')
            
    return render(req,'login.html', {"form":form})

@login_required(login_url='/')
def logout(req):
    logout(req)
    return redirect('loginn')

@login_required(login_url='')
def home(req):
    
    return render(req,'index.html')
from django.urls import include
from django.urls import path
from app.controllers import loginn

urlpatterns = [

    path('', loginn, name = 'login'),
    path('', include('app.routes'), name='app'),

]

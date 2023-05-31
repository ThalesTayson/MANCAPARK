from django.urls import include
from django.urls import path
from app.views import login

urlpatterns = [

    path('', login, name = 'login'),
    path('', include('app.urls'), name='app'),

]

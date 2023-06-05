from django.urls import path
from .controllers import *

urlpatterns = [
    
    path('home', home, name='home'),
    
]

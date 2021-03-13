from django.urls import path
from .views import *

urlpatterns=[
    path('home',home,name='home'),
    path('login',studentLogin),
    path('st',studentDashboard,name='studentDashboard'),
    path('reg',studentRegister,name='studentRegister')
]

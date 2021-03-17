from django.urls import path
from .views import *

urlpatterns=[
    path('st',studentDashboard,name='studentDashboard'),
    path('home',home,name='home'),
    path('login',studentLogin),
    path('reg',studentRegister,name='studentRegister'),
    path('test',test),
]

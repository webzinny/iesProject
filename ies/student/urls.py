from django.urls import path
from .views import *

urlpatterns=[
    path('',stDashboard,name='stDashboard'),
    path('login',studentLogin,name='login'),
    path('reg',studentRegister,name='studenRegister'),
    path('getOtp',getOtp),
    path('logout',logOut),
]

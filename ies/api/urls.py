from django.urls import path
from .views import *

urlpatterns=[
    path('validate',validate),
    path('getStudents',getStudents),
    path('teacherData',teacherData),
    path('makeatt',makeAtt),
]

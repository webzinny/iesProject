from django.contrib import admin
from .models import *

class teacherAdmin(admin.ModelAdmin):
    list_display=['id','name','email','pas']

class studentAdmin(admin.ModelAdmin):
    list_display=['id','branch','sem','sec','enroll','name','dob','email','phone','add','pas','att']

class attendanceAdmin(admin.ModelAdmin):
    list_display=['id','date','stu']

admin.site.register(teacher,teacherAdmin)
admin.site.register(student,studentAdmin)
admin.site.register(attendance,attendanceAdmin)

from django.http import JsonResponse,HttpResponse
from .models import *
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model=student
        fields=['enroll','email']

class teacherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=teacher
        fields=['id','name','email','pas']

def validate(request):
    email=request.GET['email']
    pas=request.GET['pas']
    try:
        obj=teacher.objects.get(email=email)
        if obj.pas==pas:
            return JsonResponse({'status':'ok'})
        else:
            return JsonResponse({'status':'wrong pas'})
    except:
        return JsonResponse({'status':'not found'})

def getStudents(request):
    try:
        branch=request.GET['branch']
        sem=request.GET['sem']
        sec=request.GET['sec']
        data=student.objects.filter(branch=branch,sem=sem,sec=sec)
        serializeData=studentSerializer(data,many=True)
        return JsonResponse(serializeData.data,safe=False)
    except:
        return HttpResponse("Fail")

def teacherData(request):
    data=teacher.objects.all()
    serializeData=teacherDataSerializer(data,many=True)
    return JsonResponse(serializeData.data,safe=False)

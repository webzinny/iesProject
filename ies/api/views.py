from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

def home(request):
    return render(request,'home.html')

def studentLogin(request):
    if request.method=='POST':
        enroll=request.POST['enroll']
        pas=request.POST['pas']
        try:
            obj=student.objects.get(enroll=enroll)
            if obj.pas==pas:
                return redirect('studentDashboard')
            else:
                return render(request,'home.html',{'msg':'Wrong Password'})
        except :
            return render(request,'home.html',{'msg':'Enrollment not found'})
    return redirect('home')

def studentRegister(request):
    if request.method=='POST':
        branch=request.POST['branch']
        sem=request.POST['sem']
        sec=request.POST['sec']
        enroll=request.POST['enroll']
        email=request.POST['email']
        pas=request.POST['pas']
        data=student(branch=branch,sem=sem,sec=sec,enroll=enroll,email=email,pas=pas)
        data.save()
        return HttpResponse("Registration successfull")
    return redirect('home')

def studentDashboard(request):
    return HttpResponse("login successfull")

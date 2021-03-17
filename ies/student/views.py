from django.shortcuts import render,redirect
from django.http import HttpResponse
from api.models import student,studentDetail,attendance
from .models import tempReg
from django.core.mail import send_mail
import random

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
        #--------------------------------------------------------------------------------------------------------------
        # OTP creation
        otp=""
        for i in range(4):
            otp+=str(random.randint(0,9))
        subject = 'OTP'
        message = 'Your OTP is '+otp
        email_from = 'webzinny@gmail.com'
        recipient_list = [email]
        send_mail(subject,message,email_from,recipient_list,fail_silently=False)
        #----------------------------------------------------------------------------------------------------------------
        #data=tempReg(branch=branch,sem=sem,sec=sec,enroll=enroll,email=email,pas=pas,otp=otp)
        #data.save()
        return render(request,'otpVerify.html')
    return redirect('home')

def studentDashboard(request):
    return HttpResponse("login successfull")

def test(request):
    return render(request,'otpVerify.html')

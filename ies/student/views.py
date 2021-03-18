from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from api.models import student,studentDetail,attendance
from django.core.mail import send_mail
import random

def stDashboard(request):
    if 'student' in request.session:
        data=student.objects.get(enroll=request.session['student'])
        return render(request,'stDashboard.html',{'data':data})
    return redirect('login')

def studentLogin(request):
    if request.method=='POST':
        enroll=request.POST['enroll']
        pas=request.POST['pas']
        try:
            obj=student.objects.get(enroll=enroll)
            if obj.pas==pas:
                request.session['student']=enroll
                return redirect('stDashboard')
            else:
                return render(request,'logReg.html',{'msg':'Wrong Password'})
        except :
            return render(request,'logReg.html',{'msg':'Enrollment not found'})
    return render(request,'logReg.html')

def studentRegister(request):
    if request.method=='POST':
        branch=request.POST['branch']
        sem=request.POST['sem']
        sec=request.POST['sec']
        enroll=request.POST['enroll']
        email=request.POST['email']
        name=request.POST['name']
        pas=request.POST['pas']
        data=student(branch=branch,sem=sem,sec=sec,enroll=enroll,email=email,name=name,pas=pas)
        data.save()
        request.session['student']=enroll
    return redirect('stDashboard')

def getOtp(request):
    email=request.GET['email']
    otp=""
    for i in range(4):
        otp+=str(random.randint(0,9))
    subject = 'OTP - IES | Student Adda'
    message ="Your OTP for verification is --  "+otp
    email_from = 'webzinny@zohomail.in'
    recipient_list = [email]
    send_mail(subject,message,email_from,recipient_list,fail_silently=False)
    return JsonResponse({"otp":otp});

def logOut(request):
    try:
        del request.session['student']
        return redirect ('login')
    except :
        return redirect('login')

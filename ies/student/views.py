from django.shortcuts import render,redirect
from django.http import HttpResponse
from api.models import student,studentDetail,attendance

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
        #data=student(branch=branch,sem=sem,sec=sec,enroll=enroll,email=email,pas=pas)
        #data.save()
        #--------------------------------------------------------------------------------------------------------------
        # OTP creation

        from django.core.mail import send_mail
        import random
        subject = 'OTP'
        message = 'Your OTP is '
        for i in range(4):
            message+=str(random.randint(0,9))
        email_from = 'webzinny@gmail.com'
        recipient_list = [email]
        #print(message)
        #print(email)
        send_mail(subject,message,email_from,recipient_list,fail_silently=False)
        #----------------------------------------------------------------------------------------------------------------

        return HttpResponse("Registration successfull")
    return redirect('home')

def studentDashboard(request):
    return HttpResponse("login successfull")

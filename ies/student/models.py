from django.db import models

class tempReg(models.Model):
    branch=models.CharField(max_length=5)
    sem=models.IntegerField()
    sec=models.CharField(max_length=2)
    enroll=models.CharField(max_length=10)
    email=models.EmailField()
    #name=models.CharField(max_length=50)
    pas=models.CharField(max_length=20)
    otp=models.CharField(max_length=4)

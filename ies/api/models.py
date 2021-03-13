from django.db import models

class teacher(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    pas=models.CharField(max_length=15)

class student(models.Model):
    branch=models.CharField(max_length=5)
    sem=models.IntegerField()
    sec=models.CharField(max_length=2)
    enroll=models.CharField(max_length=10)
    email=models.EmailField()
    pas=models.CharField(max_length=20)

    def __str__(self):
        return self.enroll

    def att(self):
        return [i.date for i in attendance.objects.filter(enroll=self.id)]

class studentDetail(models.Model):
    enroll=models.OneToOneField(student,on_delete=models.CASCADE,primary_key=True)
    name=models.CharField(max_length=32)
    dob=models.DateField()
    phone=models.IntegerField()
    add=models.CharField(max_length=64)

class attendance(models.Model):
    date=models.DateField()
    enroll=models.ManyToManyField(student)

    def stu(self):
        return [i.id for i in self.enroll.all()]

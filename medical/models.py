from email.policy import default
from enum import unique
from django.db import models
from autoslug import AutoSlugField
from twilio.rest import Client


# Create your models here.

class Caraousel(models.Model):
    image=models.ImageField(upload_to='image')

    

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=200)
    desc=models.CharField(max_length=500)
    

    def __str__(self):
        return self.name

class Post(models.Model):
    title=models.CharField(max_length=200,default="")
    slug=AutoSlugField(populate_from='title',unique=True,null=True,default=None)
    writer_img=models.ImageField(upload_to='image',default="")
    name=models.CharField(max_length=100,default="")
    image=models.ImageField(upload_to='image',default="")
    desc=models.TextField()
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name



class Departmentt(models.Model):
    name=models.CharField(max_length=100,default="")
    slug=AutoSlugField(populate_from='name',unique=True,null=True,default=None)
    image=models.ImageField(upload_to='image',default="")
    desc=models.TextField()

    def __str__(self):
        return self.name


class Team(models.Model):
    name=models.CharField(max_length=100,default="")
    speciality=models.CharField(max_length=100,default="")
    slug=AutoSlugField(populate_from='name',unique=True,null=True,default=None)
    image=models.ImageField(upload_to='image',default="")
    

    def __str__(self):
        return self.name


class Appointment(models.Model):
    name=models.CharField(max_length=100,default="")
    email=models.EmailField(blank=True,unique=False)
    phone=models.CharField(max_length=200)
    department=models.CharField(max_length=200)
    doctor_name=models.CharField(max_length=200)
    date=models.DateField(auto_now=False, auto_now_add=False)
    msg=models.CharField(max_length=500)
    
    def __str__(self):
        return self.name
    
    def save(self):
        account_sid = 'ACe70edc7fd6da1ba9b583c697b861025a'
        auth_token = 'aaa9e7cbcb27879cdd42d89371dcf0e1'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
                     body=f"Patient name - {self.name} and mobile Number {self.phone} appointment with Dr. {self.doctor_name}",
                     from_='+19033212013',
                     to='+917983767041'
                 )

        # print(message.sid)

        return super().save()

class Carrier(models.Model):
    carrier=models.CharField(max_length=200)
    name=models.CharField(max_length=100,default="")
    email=models.EmailField(blank=True,unique=False)
    gender=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    
    address=models.CharField(max_length=200)
    exp=models.IntegerField()
    resume=models.FileField(upload_to='news',max_length=250,null=True,default=None)
    education=models.CharField(max_length=250)
    skill=models.CharField(max_length=250)
    
    def __str__(self):
        return self.name


class Job(models.Model):
    name=models.CharField(max_length=200)
    slug=AutoSlugField(populate_from='name',unique=True,null=True,default=None)
    city=models.CharField(max_length=200)
    location=models.CharField(max_length=300)
    timing=models.CharField(max_length=100)
    salary=models.IntegerField()
    desc=models.TextField()

    def __str__(self):
        return self.name

class Feedback(models.Model):
    desc=models.TextField()

    def __str__(self):
        return self.desc


class gallary(models.Model):
    name=models.CharField(max_length=200)
    slug=AutoSlugField(populate_from='name',unique=True,null=True,default=None)
    image=models.ImageField(upload_to='image',default="")

    def __str__(self):
        return self.name

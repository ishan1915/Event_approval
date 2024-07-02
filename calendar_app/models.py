from django.db import models
from django.contrib.auth.models import User,AbstractUser

#let assume three department for now Task1=department 1,Task2=department2,task3=department3

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100, choices=[
        ('department1', 'Department 1'),
        ('department2', 'Department 2'),
        ('department3', 'Department 3'),
        # add more departments as needed
    ])

    def __str__(self):
        return self.user.username   

class Task1(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    #datetime = models.DateTimeField()
    choice_options = [
        ('6:00 AM', '6:00AM'),
        ('7:00 AM', '7:00AM'),
        ('8:00 AM', '8:00AM'),
        ('9:00 AM', '9:00AM'),
        ('10:00 AM', '10:00AM'),
        ('11:00 AM', '11:00AM'),
        ('12:00 PM', '12:00PM'),
        ('1:00 PM', '1:00PM'),
        ('2:00 PM', '2:00PM'),
        ('3:00 PM', '3:00PM'),
        ('4:00 PM', '4:00PM'),
        ('5:00 PM', '5:00PM'),
        ('6:00 PM', '6:00PM'),
        ('7:00 PM', '7:00PM'),
        ('8:00 PM', '8:00PM'),
        ('9:00 PM',  '9:00PM'),


    ]
    time = models.CharField(max_length=20, choices=choice_options)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    approved = models.BooleanField(default=False)  # For admin approval


    def __str__(self):
        #return self.title
        return f"{self.user}{self.date} {self.time} {self.title}{self.description}{self.approved}"

class Task2(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    #datetime = models.DateTimeField()
    choice_options = [
        ('6:00 AM', '6:00AM'),
        ('7:00 AM', '7:00AM'),
        ('8:00 AM', '8:00AM'),
        ('9:00 AM', '9:00AM'),
        ('10:00 AM', '10:00AM'),
        ('11:00 AM', '11:00AM'),
        ('12:00 PM', '12:00PM'),
        ('1:00 PM', '1:00PM'),
        ('2:00 PM', '2:00PM'),
        ('3:00 PM', '3:00PM'),
        ('4:00 PM', '4:00PM'),
        ('5:00 PM', '5:00PM'),
        ('6:00 PM', '6:00PM'),
        ('7:00 PM', '7:00PM'),
        ('8:00 PM', '8:00PM'),
        ('9:00 PM',  '9:00PM'),


    ]
    time = models.CharField(max_length=20, choices=choice_options)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    approved = models.BooleanField(default=False)  # For admin approval


    def __str__(self):
        #return self.title
        return f"{self.user}{self.date} {self.time} {self.title}{self.description}{self.approved}"

class Task3(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    #datetime = models.DateTimeField()
    choice_options = [
        ('6:00 AM', '6:00AM'),
        ('7:00 AM', '7:00AM'),
        ('8:00 AM', '8:00AM'),
        ('9:00 AM', '9:00AM'),
        ('10:00 AM', '10:00AM'),
        ('11:00 AM', '11:00AM'),
        ('12:00 PM', '12:00PM'),
        ('1:00 PM', '1:00PM'),
        ('2:00 PM', '2:00PM'),
        ('3:00 PM', '3:00PM'),
        ('4:00 PM', '4:00PM'),
        ('5:00 PM', '5:00PM'),
        ('6:00 PM', '6:00PM'),
        ('7:00 PM', '7:00PM'),
        ('8:00 PM', '8:00PM'),
        ('9:00 PM',  '9:00PM'),


    ]
    time = models.CharField(max_length=20, choices=choice_options)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    approved = models.BooleanField(default=False)  # For admin approval


    def __str__(self):
        #return self.title
        return f"{self.user}{self.date} {self.time} {self.title}{self.description}{self.approved}"

 

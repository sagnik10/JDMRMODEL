from django.db import models

class School(models.Model):
    Gender = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('binary', 'Binary'),
    )
    Year_Established = models.CharField(max_length=50)
    School_Type = models.CharField(max_length=200)
    gender = models.CharField(choices = Gender,max_length=8)
    Boarding = models.CharField(max_length=50)
    Grades = models.CharField(max_length=200)
    Admission_Period = models.CharField(max_length=200)
    Curriculum = models.CharField(max_length = 100)
    School_Level = models.CharField(max_length = 100)
    Description = models.TextField(max_length = 1000)

    def __str__(self):
        return self.Year_Established

class Address_Contacts(models.Model):

    School_Address = models.CharField(max_length=50)
    School_Chairman_Principal = models.CharField(max_length=200)
    Phone_Number = models.CharField(max_length=50)
    Email_Address = models.EmailField(max_length=200)
    School_Website = models.CharField(max_length = 200)

    def __str__(self):
        return self.School_Address


class Admission_Enquiry(models.Model):
    Class = (
        ('Class LKG', 'Class LKG'),
        ('Class PRE KG', 'Class PRE KG'),
        ('Class UKG', 'Class UKG'),
        ('Class I', 'Class I'),
        ('Class II', 'Class II'),
        ('Class III', 'Class III'),
        ('Class IV', 'Class IV'),
        ('Class V', 'Class V'),

    )
    Name = models.CharField(max_length=50)
    Email_Address = models.EmailField(max_length=200)
    Phone_Number = models.CharField(max_length=50)
    Your_Message = models.TextField(max_length = 1000)
    gender = models.CharField(choices = Class,max_length=20)

    def __str__(self):
        return self.Name

class Admission_Details(models.Model):
    Academic_Year = models.CharField(max_length=100)
    Admission_Period = models.CharField(max_length=100)
    Fee_Details = models.CharField(max_length=500)
    Description = models.TextField(max_length=1000)

    def __str__(self):
        return self.Academic_Year

class admission(models.Model):
    classname = models.CharField(max_length=150)
    session = models.CharField(max_length=50)
    last_date = models.CharField(max_length=50)
    Application_Fees = models.IntegerField()

    def __str__(self):
        return self.classname

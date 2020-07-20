from django.db import models

#This is store the all the enterprises
class Enterprise(models.Model):
    enterpriseId = models.AutoField(primary_key=True, unique=True)
    enterpriseName = models.CharField(max_length=250)
    enterpriseAddress = models.CharField(max_length=250)
    enterpriseEmailAddress = models.EmailField(max_length=250, unique=True)
    enterpriseContactNumber = models.CharField(max_length=10)
    enterpriseGSTNumber = models.CharField(max_length=50, unique=True)
    enterpriseType = models.CharField(max_length=150)
    dateOfRegistration = models.DateField(auto_now=True, auto_created=True)
    timeOfRegistration = models.TimeField(auto_now=True, auto_created=True)
    enterpriseWebsite = models.URLField()
    enterpriseDetails = models.CharField(max_length=500)


#This is for the users with Admin Access
class AdminUser(models.Model):
    adminId = models.CharField(max_length=150, primary_key=True, unique=True)
    enterpriseId = models.ForeignKey(Enterprise, default=None, on_delete=models.CASCADE)
    adminName = models.CharField(max_length=250)
    Password = models.CharField(max_length=250)

    def __str__(self):
        return self.adminId

#This is to store all the Staff
class Employee(models.Model):
    employeeId = models.CharField(primary_key=True, unique=True, max_length=150)
    employeeName = models.CharField(max_length=200, blank=False)
    password = models.CharField(max_length=250)
    enterpriseId = models.ForeignKey(Enterprise, default=None, on_delete=models.CASCADE)
    contactNumber = models.CharField(max_length=10, unique=True)
    emailAddress = models.EmailField(max_length=250, unique=True)
    aadhaarNumber = models.CharField(max_length=20, unique=True)
    panNumber = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.employeeId



#This is to store all the tenants
class Tenant(models.Model):
    tenantId = models.CharField(primary_key=True, unique=True, max_length=150)
    tenantName = models.CharField(max_length=200, blank=False)
    password = models.CharField(max_length=250)
    enterpriseId = models.ForeignKey(Enterprise, default=None, on_delete=models.CASCADE)
    contactNumber = models.CharField(max_length=10, unique=True)
    emailAddress = models.EmailField(max_length=250, unique=True)
    aadhaarNumber = models.CharField(max_length=20, unique=True)
    panNumber = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.tenantId


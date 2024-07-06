from django.db import models

# Create your models here.
class UserMaster(models.Model):
    UserId=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    Phone=models.BigIntegerField()
    Password=models.CharField(max_length=100)
    Gender=models.CharField(max_length=10)
    Role=models.CharField(max_length=20)
    Status=models.CharField(max_length=20,default='active')



class Leave(models.Model):
    LeaveId=models.AutoField(primary_key=True)
    LeaveType=models.CharField(max_length=5)
    LeaveDays=models.IntegerField()


class ApplyLeave(models.Model):
    ApplyLeaveId=models.AutoField(primary_key=True)
    UserId=models.ForeignKey(UserMaster,default=None,on_delete=models.CASCADE)
    LeaveId=models.ForeignKey(Leave,default=None,on_delete=models.CASCADE)
    ToDate=models.DateField()
    FromDate=models.DateField()
    Reason=models.CharField(max_length=200)
    LeaveStatus=models.CharField(max_length=20,default='NotApproved')
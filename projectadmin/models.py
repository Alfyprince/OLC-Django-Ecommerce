from django.db import models
from django.utils import timezone
# Create your models here.
class projectadmin(models.Model):
    Email=models.CharField(max_length=50)
    Password=models.CharField(max_length=20)

    def __str__(self) :
        return self.Email
    

class products(models.Model):
    pname=models.CharField(max_length=500)
    ptype=models.CharField(max_length=500)
    price=models.FloatField(null=True)
    category=models.CharField(max_length=500,null=True)
    warranty=models.CharField(max_length=200)
    quantity=models.IntegerField(null=True)
    company=models.CharField(max_length=200,null=True)
    photo=models.CharField(max_length=200,null=True)
    desc=models.CharField(max_length=500)
    avgrate=models.CharField(max_length=500,null=True)
    rlength=models.CharField(max_length=500,default=0)

    def __str__(self) :
        return self.pname
    
# class products1(models.Model):0
#     pname=models.CharField(max_length=50)
#     ptype=models.CharField(max_length=50)
#     price=models.CharField(max_length=20)
#     warranty=models.CharField(max_length=20)
#     photo=models.CharField(max_length=200)
#     quantity=models.CharField(max_length=20)
#     company=models.CharField(max_length=20)
#     desc=models.CharField(max_length=500)

#     def __str__(self) :
#         return self.pname

class prod(models.Model):
    pname=models.CharField(max_length=50)
    ptype=models.CharField(max_length=50)
    company=models.CharField(max_length=50,null=True)
    category=models.CharField(max_length=50,null=True)
    price=models.FloatField(null=True)
    quantity=models.IntegerField(null=True)
    total=models.IntegerField(null=True)
    orddate=models.DateField(default=timezone.now)
    deldate=models.DateField(null=True)
    accdate=models.DateField(null=True)
    accept=models.BooleanField(default=False)
    reject=models.BooleanField(default=False)
    payment=models.BooleanField(default=False)
    admin=models.ForeignKey(projectadmin,on_delete=models.CASCADE)
    warranty=models.CharField(max_length=20,null=True)
    photo=models.ImageField(upload_to='prod',null=True)

    def __str__(self) :
        return self.pname


class attendance(models.Model):
    status=models.CharField(max_length=20,null=True)
    staffs=models.CharField(max_length=20,null=True)
    date=models.CharField(max_length=20,null=True)
    

    def __str__(self) :
        return self.date
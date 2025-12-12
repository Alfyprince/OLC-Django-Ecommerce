from django.db import models
from django.utils import timezone
from projectadmin.models import *
# Create your models here.
class customer(models.Model):
    Cname=models.CharField(max_length=20)
    Phoneno=models.CharField(max_length=10)
    Email=models.CharField(max_length=50)
    Homename=models.CharField(max_length=50)
    Location=models.CharField(max_length=50)
    Pincode=models.CharField(max_length=50)
    Photo=models.ImageField(upload_to="customer")
    Password=models.CharField(max_length=20)
    accept=models.BooleanField(default=False)
    reject=models.BooleanField(default=False)
    

    def __str__(self) :
        return self.Cname
    



class booking(models.Model):
    pname=models.CharField(max_length=20)
    price=models.FloatField()
    ptype=models.CharField(max_length=50)
    customer=models.ForeignKey(customer,on_delete=models.CASCADE)
    product=models.ForeignKey(products,on_delete=models.CASCADE,null=True)
    date=models.DateField(default=timezone.now)
    quantity=models.IntegerField()
    accept=models.BooleanField(default=False)
    reject=models.BooleanField(default=False)
    book=models.BooleanField(default=False)
    payment=models.BooleanField(default=False)
    delivered=models.BooleanField(default=False)
    company=models.CharField(max_length=50,null=True)
    

    def __str__(self) :
        return self.pname



class complaints(models.Model):
    pname=models.CharField(max_length=20)
    ptype=models.CharField(max_length=50)
    company=models.CharField(max_length=50,null=True)
    reply=models.CharField(max_length=50,null=True)
    complaint=models.CharField(max_length=200)
    customer=models.ForeignKey(customer,on_delete=models.CASCADE)
    date=models.DateField(default=timezone.now)
    send=models.BooleanField(default=False)
    action=models.BooleanField(default=False)
    

    def __str__(self) :
        return self.pname
    

class prodrate(models.Model):
    rate=models.CharField(max_length=500)
    review=models.CharField(max_length=200)
    product=models.ForeignKey(products,on_delete=models.CASCADE)
    customers=models.ForeignKey(customer,on_delete=models.CASCADE)

    def __str__(self) :
        return self.rate
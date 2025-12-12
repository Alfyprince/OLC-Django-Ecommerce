from django.db import models
from django.utils import timezone
# Create your models here.
class staff(models.Model):
    staffname=models.CharField(max_length=20)
    Phoneno=models.CharField(max_length=10)
    Email=models.CharField(max_length=50)
    Homename=models.CharField(max_length=50)
    place=models.CharField(max_length=20)
    Location=models.CharField(max_length=50)
    Pincode=models.CharField(max_length=50)
    Photo=models.ImageField(upload_to="staff")
    proof=models.ImageField(upload_to="staff",null=True)
    Password=models.CharField(max_length=20)
    accept=models.BooleanField(default=False)
    reject=models.BooleanField(default=False)
    

    def __str__(self) :
        return self.staffname
    



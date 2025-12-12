from django.db import models

# Create your models here.
class company(models.Model):
    Comname=models.CharField(max_length=20)
    Phoneno=models.CharField(max_length=10)
    Email=models.CharField(max_length=50)
    Place=models.CharField(max_length=20)
    District=models.CharField(max_length=20)
    Location=models.CharField(max_length=50)
    Pincode=models.CharField(max_length=50)
    Photo=models.ImageField(upload_to="company")
    Password=models.CharField(max_length=20)
    accept=models.BooleanField(default=False)
    reject=models.BooleanField(default=False)
    

    def __str__(self) :
        return self.Comname


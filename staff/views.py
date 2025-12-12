from django.shortcuts import render,redirect
from .models import *
from customer.models import *
from projectadmin.models import *
from django.contrib import messages
import os
from datetime import date,datetime
# Create your views here.
def staffreg(request):
    if request.method=="POST":

        staffname=request.POST.get('staffname')
        Phoneno=request.POST.get('Phoneno')
        Email=request.POST.get('Email')
        Homename=request.POST.get('Homename')
        place=request.POST.get('place')
        Pincode=request.POST.get('Pincode')
        Location=request.POST.get('Location')
        Photo=request.FILES.get('Photo')
        proof=request.FILES.get('proof')
        Password=request.POST.get('password')
        RePassword=request.POST.get('cpassword')
        if Password==RePassword:
            if staff.objects.filter(Phoneno=Phoneno).exists():
                messages.info(request,'PhoneNumber Already Exits')
            elif staff.objects.filter(Email=Email).exists():
                messages.info(request,'EmailPhoto Address Already Exits')
            else:
                reg=staff(staffname=staffname,Location=Location,Photo=Photo,Email=Email,
                             Phoneno=Phoneno,Homename=Homename,place=place,Password=Password,Pincode=Pincode,proof=proof)
                reg.save()
                # print("values uploaded")
                return redirect('stafflog')
    
    return render(request,'staff/sreg.html')


def stafflog(request):
    error_message= None
    if request.method=="POST":
        try:
            Email=request.POST.get('Email')
            Password=request.POST.get('Password')
            log=staff.objects.get(Email=Email,Password=Password)
            if log.accept:
                request.session['staffname']=log.staffname
                request.session['id']=log.id

                return redirect('staffhome')
            else:
                messages.info(request,'Account Blocked')
        except staff.DoesNotExist as e:
            messages.info(request,'Invalid User')

    return render(request,'staff/slogin.html',{'error':error_message})

def staffhome(request):
    id=request.session['id']
    pro=staff.objects.get(id=id)
    return render(request,'staff/sindex.html',{'pro':pro})







def sprofile(request):
    id=request.session['id']
    pro=staff.objects.get(id=id)
    return render(request,'staff/sprofile.html',{'pd':pro})



def seditprof(request,id):
    edit=staff.objects.get(id=id)
    if request.method=="POST":
        if len(request.FILES)!=0:
            if len(edit.Photo)>0:
                os.remove(edit.Photo.path)
            edit.Photo=request.FILES["Photo"]    
        edit.staffname = request.POST.get('staffname')
        edit.Phoneno = request.POST.get('Phoneno')
        edit.Email = request.POST.get('Email')
        edit.Homename = request.POST.get('Homename')
        edit.Location = request.POST.get('Location')
        edit.Pincode = request.POST.get('Pincode')
        edit.Password = request.POST.get('password')
        edit.save()
        return redirect('staffhome')
    return render(request,"staff/seditprof.html",{"edit":edit})




def satten(request):
    id=request.session['id']
    sta=staff.objects.get(id=id)
    st=sta.staffname
    pro=attendance.objects.filter(staffs=st)
    return render(request,'staff/sattendance.html',{'pro':pro})


def prodbkd(request):
    day=date.today()
    id=request.session['id']
    sta=staff.objects.get(id=id)
    st=sta.staffname
    pro=booking.objects.filter(payment=True,delivered=False)
    pros=attendance.objects.filter(staffs=st,date=day,status="Present")
    return render(request,'staff/bookedprds.html',{'pro':pro,'pros':pros})

def delivered(request,id):
    booking.objects.filter(id=id).update(delivered=True)
    return redirect('staffhome')
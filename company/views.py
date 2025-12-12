from django.shortcuts import render,redirect
from .models import *
from customer.models import *
from projectadmin.models import *
from django.contrib import messages
from django.db.models import Q
import os
from datetime import date
# Create your views here.
def comreg(request):
    if request.method=="POST":

        Comname=request.POST.get('Comname')
        Phoneno=request.POST.get('Phoneno')
        Email=request.POST.get('Email')
        Place=request.POST.get('Place')
        District=request.POST.get('District')
        Pincode=request.POST.get('Pincode')
        Location=request.POST.get('Location')
        Photo=request.FILES.get('Photo')
        Password=request.POST.get('password')
        RePassword=request.POST.get('cpassword')
        if Password==RePassword:
            if company.objects.filter(Phoneno=Phoneno).exists():
                messages.info(request,'PhoneNumber Already Exits')
            elif company.objects.filter(Email=Email).exists():
                messages.info(request,'EmailPhoto Address Already Exits')
            else:
                reg=company(Comname=Comname,Place=Place,District=District,Location=Location,Photo=Photo,Email=Email,
                             Phoneno=Phoneno,Password=Password,Pincode=Pincode)
                reg.save()
                # print("values uploaded")
                return redirect('comlog')
    
    return render(request,'company/comreg.html')


def comlog(request):
    error_message= None
    if request.method=="POST":
        try:
            Email=request.POST.get('Email')
            Password=request.POST.get('Password')
            log=company.objects.get(Email=Email,Password=Password)
            if log.accept:
                request.session['Comname']=log.Comname
                request.session['id']=log.id

                return redirect('companyhome')
            else:
                messages.info(request,'Account Blocked')
        except company.DoesNotExist as e:
            messages.info(request,'Invalid User')

    return render(request,'company/comlogin.html',{'error':error_message})

def companyhome(request):
    id=request.session['id']
    pro=company.objects.get(id=id)
    return render(request,'company/comindex.html',{'pro':pro})



def vprods(request):
    id=request.session['id']
    com=company.objects.get(id=id)
    comp=com.Comname
    pro=prod.objects.filter(company=comp,accept=False,reject=False,payment=False)
    return render(request,'company/viewprods.html',{'pro':pro,'comp':comp,'com':com})


def accept(request,id):
    cid=request.session['id']
    com=company.objects.get(id=cid)
    pro=prod.objects.get(id=id)
    qua=pro.quantity
    day=date.today()
    if request.method=="POST":
        
        pro.photo=request.FILES.get('photo')
        pro.price=request.POST.get('price')
        pro.warranty=request.POST.get('warranty')
        pro.deldate=request.POST.get('deldate')
        pro.total=int(pro.price)*int(qua)
        pro.save()
        prod.objects.filter(id=id).update(accept=True)
        prod.objects.filter(id=id).update(reject=False)
        prod.objects.filter(id=id).update(payment=False)
        prod.objects.filter(id=id).update(accdate=day)

        return redirect('companyhome')
    return render(request,'company/crstprod.html',{'com':com,'pro':pro})


def reject(request,id):
    prod.objects.filter(id=id).update(reject=True)
    prod.objects.filter(id=id).update(accept=False)
    prod.objects.filter(id=id).update(payment=False)
    return redirect('companyhome')



def accprods(request):
    id=request.session['id']
    com=company.objects.get(id=id)
    comp=com.Comname
    pro=prod.objects.filter(company=comp,accept=True)
    # pro=prod.objects.filter(Q(accept=True) | Q(payment=True))
    # pro=prod.objects.filter(Q(accept=True) | Q(payment=True))
    return render(request,'company/acptprod.html',{'pro':pro,'comp':comp,'com':com})


def remove(request,id):
    pro=prod.objects.filter(id=id)
    rem=pro.delete()
    return redirect('companyhome')




def comprofile(request):
    id=request.session['id']
    pro=company.objects.get(id=id)
    return render(request,'company/comprofile.html',{'pd':pro})


def comeditprof(request,id):
    edit=company.objects.get(id=id)
    if request.method=="POST":
        if len(request.FILES)!=0:
            if len(edit.Photo)>0:
                os.remove(edit.Photo.path)
            edit.Photo=request.FILES["Photo"]    
        edit.Comname = request.POST.get('Comname')
        edit.Phoneno = request.POST.get('Phoneno')
        edit.Email = request.POST.get('Email')
        edit.Location = request.POST.get('Location')
        edit.Pincode = request.POST.get('Pincode')
        edit.Password = request.POST.get('password')
        edit.save()
        return redirect('companyhome')
    return render(request,"company/comeditprof.html",{"edit":edit})


def viewcopml(request):
    id=request.session['id']
    pro=company.objects.get(id=id)
    com=pro.Comname
    prof=complaints.objects.filter(company=com,send=True)
    return render(request,'company/viewcomplaint.html',{'prof':prof,'com':com})


def reply(request,id):
    pro=complaints.objects.get(id=id)
    if request.method=="POST":
        reply=request.POST.get('reply')
        complaints.objects.filter(id=id).update(reply=reply)
        return redirect('companyhome')
    return render(request,'company/reply.html')
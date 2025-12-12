from django.shortcuts import render,redirect
from .models import *
from projectadmin.models import *
from django.contrib import messages
from django.db.models import Q
from olc.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY
import razorpay
import os
# Create your views here.
def creg(request):
    if request.method=="POST":
        
        Cname=request.POST.get('Cname')
        Phoneno=request.POST.get('Phoneno')
        Email=request.POST.get('Email')
        Homename=request.POST.get('Homename')
        Pincode=request.POST.get('Pincode')
        Location=request.POST.get('Location')
        Photo=request.FILES.get('Photo')
        Password=request.POST.get('password')
        RePassword=request.POST.get('cpassword')
        if Password==RePassword:
            if customer.objects.filter(Phoneno=Phoneno).exists():
                messages.info(request,'PhoneNumber Already Exits')
            elif customer.objects.filter(Email=Email).exists():
                messages.info(request,'Email Already Exits')
            else:
                reg=customer(Cname=Cname,Location=Location,Photo=Photo,Email=Email,
                             Phoneno=Phoneno,Homename=Homename,Password=Password,Pincode=Pincode)
                reg.save()
                # print("values uploaded")
                return redirect('clog')
    
    return render(request,'customer/creg.html')


def clog(request):
    error_message= None
    if request.method=="POST":
        try:
            Email=request.POST.get('Email')
            Password=request.POST.get('Password')
            log=customer.objects.get(Email=Email,Password=Password)
            # if log.accept:
            request.session['Cname']=log.Cname
            request.session['id']=log.id

            return redirect('chome')
            # else:
            #     messages.info(request,'Account Blocked')
        except customer.DoesNotExist as e:
            messages.info(request,'Invalid User')

    return render(request,'customer/clogin.html',{'error':error_message})

def chome(request):
    id=request.session['id']
    pro=customer.objects.get(id=id)
    return render(request,'customer/cindex.html',{'pro':pro})


def vunddf(request):
    pro=products.objects.filter(pname= "Underground Drainage Fittings")
    return render(request,'customer/viewprod.html',{'pro':pro})


def vswrds(request):
    pro=products.objects.filter(pname= "SWR Drainage System")
    return render(request,'customer/viewprod.html',{'pro':pro})


def vrainwh(request):
    pro=products.objects.filter(pname= "Rain Water Harvester")
    return render(request,'customer/viewprod.html',{'pro':pro})


def vcpvc(request):
    pro=products.objects.filter(pname= "CPVC Pipes & Fittings")
    return render(request,'customer/viewprod.html',{'pro':pro})


def vpvc(request):
    pro=products.objects.filter(pname= "PVC Pipes & Fittings")
    return render(request,'customer/viewprod.html',{'pro':pro})

def vupvc(request):
    pro=products.objects.filter(pname= "uPVC Pipes & Fittings")
    return render(request,'customer/viewprod.html',{'pro':pro})


def vlight(request):
    pro=products.objects.filter(pname= "LED LIGHTS")
    return render(request,'customer/vlightcat.html',{'pro':pro})


def vfan(request):
    pro=products.objects.filter(pname= "Fan")
    return render(request,'customer/vfancat.html',{'pro':pro})

def virons(request):
    pro=products.objects.filter(pname= "IRONS")
    return render(request,'customer/Virons.html',{'pro':pro})

def vmixer(request):
    pro=products.objects.filter(pname= "KITCHEN APPLIANCES")
    return render(request,'customer/viewprod.html',{'pro':pro})


def vswitch(request):
    pro=products.objects.filter(pname= "SWITCHES AND ACCESSORIES")
    return render(request,'customer/viewprod.html',{'pro':pro})

def vtank(request):
    pro=products.objects.filter(pname= "WATER TANK")
    return render(request,'customer/vtank.html',{'pro':pro})

def vswitch(request):
    pro=products.objects.filter(pname= "SWITCHES AND ACCESSORIES")
    return render(request,'customer/vswitch.html',{'pro':pro})

def vtap(request):
    pro=products.objects.filter(pname= "TAP")
    return render(request,'customer/vtapcat.html',{'pro':pro})


def vsatr(request):
    pro=products.objects.filter(Q(pname= "Thread seal Tape") | Q(pname="Star Bond GOLD") | Q(pname="Solvent Cement Normal") | Q(pname="Star Bond"))
    return render(request,'customer/viewprod.html',{'pro':pro})



def dryiron(request):
    pro=products.objects.filter(Q(category__iexact= "dry iron") | Q(category__iexact= "dry irons"))
    return render(request,'customer/viewprod.html',{'pro':pro})


def steamiron(request):
    pro=products.objects.filter(Q(category__iexact= "steam iron") | Q(category__iexact= "steam irons"))
    return render(request,'customer/viewprod.html',{'pro':pro})


def hanglight(request):
    pro=products.objects.filter(Q(category__iexact= "Indoor Hanging Light") | Q(category__iexact= "Indoor Hanging Lights"))
    return render(request,'customer/viewprod.html',{'pro':pro})


def walllight(request):
    pro=products.objects.filter(Q(category__iexact= "Indoor Wall Light") | Q(category__iexact= "Indoor Wall Lights"))
    return render(request,'customer/viewprod.html',{'pro':pro})


def mirrlight(request):
    pro=products.objects.filter(Q(category__iexact= "Mirror Light") | Q(category__iexact= "mirror Lights"))
    return render(request,'customer/viewprod.html',{'pro':pro})


def floodlight(request):
    pro=products.objects.filter(Q(category__iexact= "Flood Light") | Q(category__iexact= "Flood Lights"))
    return render(request,'customer/viewprod.html',{'pro':pro})


def zoomlight(request):
    pro=products.objects.filter(Q(category__iexact= "Zoom Lights") | Q(category__iexact= "Zoom Light"))
    return render(request,'customer/viewprod.html',{'pro':pro})


def panellight(request):
    pro=products.objects.filter(Q(category__iexact= "Panel Lights") | Q(category__iexact= "Panel Light"))
    return render(request,'customer/viewprod.html',{'pro':pro})


def glowlight(request):
    pro=products.objects.filter(Q(category__iexact= "High Glow Light") | Q(category__iexact= "High Glow Lights"))
    return render(request,'customer/viewprod.html',{'pro':pro})


def filalight(request):
    pro=products.objects.filter(Q(category__iexact= "filament Light") |Q(category__iexact= "filament Lights"))
    return render(request,'customer/viewprod.html',{'pro':pro})


def tubelight(request):
    pro=products.objects.filter(Q(category__iexact= "Tube Light") | Q(category__iexact= "Tube Lights"))
    return render(request,'customer/viewprod.html',{'pro':pro})




def ceilfan(request):
    pro=products.objects.filter(Q(category__iexact= "Ceiling Fans") | Q(category__iexact= "Ceiling Fan"))
    return render(request,'customer/viewprod.html',{'pro':pro})



def tablefan(request):
    pro=products.objects.filter(Q(category__iexact= "Table Fans") | Q(category__iexact= "Table Fan"))
    return render(request,'customer/viewprod.html',{'pro':pro})



def pedestalfan(request):
    pro=products.objects.filter(Q(category__iexact= "Pedestal Fans") | Q(category__iexact= "Pedestal Fan"))
    return render(request,'customer/viewprod.html',{'pro':pro})



def wallfan(request):
    pro=products.objects.filter(Q(category__iexact= "Wall Fans") | Q(category__iexact= "Wall Fan"))
    return render(request,'customer/viewprod.html',{'pro':pro})



def domfan(request):
    pro=products.objects.filter(Q(category__iexact= "Domestic Exhaust Fans") | Q(category__iexact= "Domestic Exhaust Fan"))
    return render(request,'customer/viewprod.html',{'pro':pro})



def perfan(request):
    pro=products.objects.filter(Q(category__iexact= "Personal Fans") | Q(category__iexact= "Personal Fan"))
    return render(request,'customer/viewprod.html',{'pro':pro})



def mountfan(request):
    pro=products.objects.filter(Q(category__iexact= "Ceiling Mounting Fans") | Q(category__iexact= "Ceiling Mounting Fan"))
    return render(request,'customer/viewprod.html',{'pro':pro})



def tape(request):
    pro=products.objects.filter(Q(category__iexact= "Tape") | Q(category__iexact= "Tape"))
    return render(request,'customer/viewprod.html',{'pro':pro})



def staintap(request):
    pro=products.objects.filter(Q(category__iexact= "Stainless Tap") | Q(category__iexact= "Stainless Taps")| Q(category__iexact= "Stain less Taps")| Q(category__iexact= "Stain less Tap"))
    return render(request,'customer/viewprod.html',{'pro':pro})



def plastic(request):
    pro=products.objects.filter(Q(category__iexact= "Plastic Tap") | Q(category__iexact= "Plastics Taps"))
    return render(request,'customer/viewprod.html',{'pro':pro})




def tank(request):
    pro=products.objects.filter(Q(category__iexact= "Tank") | Q(category__iexact= "Tank"))
    return render(request,'customer/viewprod.html',{'pro':pro})



def silktank(request):
    pro=products.objects.filter(Q(category__iexact= "Siltank Covers") | Q(category__iexact= "Siltank Cover"))
    return render(request,'customer/viewprod.html',{'pro':pro})




def lofttank(request):
    pro=products.objects.filter(Q(category__iexact= "Loft Tank") | Q(category__iexact= "Loft Tank"))
    return render(request,'customer/viewprod.html',{'pro':pro})




def ltankcov(request):
    pro=products.objects.filter(Q(category__iexact= "Loft Tank Cover") | Q(category__iexact= "Loft Tank Cover"))
    return render(request,'customer/viewprod.html',{'pro':pro})





def wirecable(request):
    pro=products.objects.filter(Q(category__iexact= "WIRES & CABLES") | Q(category__iexact= "WIRES & CABLES"))
    return render(request,'customer/viewprod.html',{'pro':pro})




def switchgears(request):
    pro=products.objects.filter(Q(category__iexact= "SWITCHGEARS") | Q(category__iexact= "SWITCHGEARS"))
    return render(request,'customer/viewprod.html',{'pro':pro})

def accessories(request):
    pro=products.objects.filter(Q(category__iexact= "ACCESSORIES") | Q(category__iexact= "ACCESSORIES"))
    return render(request,'customer/viewprod.html',{'pro':pro})





def switchaccessories(request):
    pro=products.objects.filter(Q(category__iexact= "SWITCHES") | Q(category__iexact= "SWITCHES"))
    return render(request,'customer/viewprod.html',{'pro':pro})



def prodet(request,id):
    pro=products.objects.get(id=id)
    return render(request,'customer/prodetail.html',{'pd':pro})


def cprof(request):
    id=request.session['id']
    pro=customer.objects.get(id=id)
    return render(request,'customer/cprofile.html',{'pd':pro})



def prodcat(request):
    return render(request,'customer/vprodcat.html')



def book(request,id):
    pro=products.objects.get(id=id)
    # qua=pro.quantity
    if request.method=="POST":
        
        pname=request.POST.get('pname')
        price=request.POST.get('price')
        ptype=request.POST.get('ptype')
        company=request.POST.get('company')
        quantity=request.POST.get('quantity')
        qua=request.POST.get('qua')
        cid=request.session['id']
        product=id
        if quantity>qua:
            messages.info(request,'Quantity insufficient')
        else:
            reg=booking(pname=pname,price=price,ptype=ptype,company=company,
                    quantity=quantity,customer_id=cid,book=True,product_id=product)
            reg.save()
            qua=int(pro.quantity) - int(quantity)
            products.objects.filter(id=id).update(quantity=qua)
            # print("values uploaded")
            return redirect('chome')
    
    return render(request,'customer/booking.html',{'pro':pro})


def ccart(request):
    id=request.session['id']
    menu=booking.objects.filter(customer=id,payment=False)
    global amount
    sum=tax=total=0  
    amount=0        
    for i in menu:
            # global amount
            sum += float(i.price) * int(i.quantity)
            tax=sum*.18
            total=sum+tax
            amount=total
    return render(request,'customer/cart.html',{'menu':menu,'sum':sum,'amount':amount,'tax':tax,'total':total})

def remove(request,id):
    dele=booking.objects.filter(id=id)
    d=dele.delete()
    return redirect('chome')



client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))

def cpayment(request):
    global amount
    id=request.session['id']
    booking.objects.filter(customer=id).update(payment=True)
    currency ="INR"
    api_key=RAZORPAY_API_KEY
    amt=int(amount)*100
    payment_order= client.order.create(dict(amount=amt,currency="INR",payment_capture=1))
    payment_order_id= payment_order['id'] 
    return render(request,'customer/payment.html',{'a':amount,'api_key':api_key,'order_id':payment_order_id})



def editprof(request,id):
    edit=customer.objects.get(id=id)
    if request.method=="POST":
        if len(request.FILES)!=0:
            if len(edit.Photo)>0:
                os.remove(edit.Photo.path)
            edit.p_img=request.FILES["Photo"]    
        edit.Cname = request.POST.get('Cname')
        edit.Phoneno = request.POST.get('Phoneno')
        edit.Email = request.POST.get('Email')
        edit.Homename = request.POST.get('Homename')
        edit.Location = request.POST.get('Location')
        edit.Pincode = request.POST.get('Pincode')
        edit.Password = request.POST.get('password')
        edit.save()
        return redirect('chome')
    return render(request,"customer/editprof.html",{"edit":edit})



def bkdprod(request):
    id=request.session['id']
    pro=booking.objects.filter(customer=id,payment=True)
    return render(request,'customer/bkdprods.html',{'pro':pro})




def complaint(request,id):
    pro=booking.objects.get(id=id)
    if request.method=="POST":
        
        pname=request.POST.get('pname')
        complaint=request.POST.get('complaint')
        company=request.POST.get('company')
        ptype=request.POST.get('ptype')
        cid=request.session['id']
        reg=complaints(pname=pname,complaint=complaint,ptype=ptype,customer_id=cid,company=company)
        reg.save()
        return redirect('chome')
    
    return render(request,'customer/complaint.html',{'pro':pro})



def prorate(request,id):
    h=booking.objects.get(id=id)
    pid=h.product.id
    if request.method=="POST":
        
        rate=request.POST['rate'] 
        review=request.POST['Suggestions']
        hid=h.product.id
        uid=request.session['id']
        value=prodrate(rate=rate,review=review,product_id=hid,customers_id=uid)
        value.save()
        # data=rating.objects.get(Filmid=id)
        # pid=data.producerId
        data=prodrate.objects.filter(product=pid)
        length=len(data)
        # trate=[]
        x=0
        for i in data:
            x=int(i.rate)+x
        
        trate=int(round(x/length))
        products.objects.filter(id=pid).update(avgrate=trate)
        products.objects.filter(id=pid).update(rlength=length)
        return redirect('chome')
    
    return render(request,'customer/prodrate.html',{'h':h})




def vcomplaint(request):
    id=request.session['id']
    pro=complaints.objects.filter(customer=id)
    return render(request,'customer/vcomplts.html',{'pro':pro})



def cbill(request,id):
    pro=booking.objects.filter(id=id)
    sum=0  
    for i in pro:
            sum += float(i.price) * int(i.quantity)
    return render(request,'customer/cbill.html',{'pro':pro,'sum':sum})
from django.shortcuts import render,redirect
from .models import *
from company.models import *
from staff.models import *
from customer.models import *
from django.contrib import messages
from olc.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY
import razorpay
from datetime import datetime,date
import json
from collections import defaultdict
from django.db.models import Sum,F,Count
# Create your views here.
def adminreg(request):
    if request.method=="POST":
        
        
        Email=request.POST.get('email')
        Password=request.POST.get('password')
        RePassword=request.POST.get('cpassword')
        if Password==RePassword:
            
            if projectadmin.objects.filter(Email=Email).exists():
                messages.info(request,'Email Already Exits')
            else:
                reg=projectadmin(Email=Email,Password=Password)
                reg.save()
                # print("values uploaded")
                return redirect('adminlog')
    
    return render(request,'admin/signup.html')


def adminlog(request):
    error_message= None
    if request.method=="POST":
        try:
            Email=request.POST.get('email')
            Password=request.POST.get('password')
            log=projectadmin.objects.get(Email=Email,Password=Password)
            # if log.accept:
            request.session['email']=log.Email
            request.session['id']=log.id

            return redirect('adminhome')
            # else:
            #     messages.info(request,'Account Blocked')
        except projectadmin.DoesNotExist as e:
            messages.info(request,'Invalid User')

    return render(request,'admin/signin.html',{'error':error_message})

def adminhome(request):
    com=company.objects.all()
    cust=customer.objects.all()
    sta=staff.objects.all()
    return render(request,'admin/index.html',{'com':com,'cust':cust,'sta':sta})


def table(request):
    com=company.objects.all()
    cust=customer.objects.all()
    sta=staff.objects.all()
    return render(request,'admin/table.html',{'com':com,'cust':cust,'sta':sta})

def comaccept(request,id):
    company.objects.filter(id=id).update(accept=True)
    company.objects.filter(id=id).update(reject=False)
    return redirect('adminhome')


def comreject(request,id):
    data=company.objects.filter(id=id)
    data.delete()
    return redirect('adminhome')



def saccept(request,id):
    staff.objects.filter(id=id).update(accept=True)
    staff.objects.filter(id=id).update(reject=False)
    return redirect('adminhome')



def sreject(request,id):
    data=staff.objects.filter(id=id)
    data.delete()
    return redirect('adminhome')

def addprod(request,id):
    pro=prod.objects.get(id=id)
    if request.method=="POST":
        
        
        pname=request.POST.get('pname')
        ptype=request.POST.get('ptype')
        price=request.POST.get('price')
        warranty=request.POST.get('warranty')
        photo=request.POST.get('photo')
        quantity=request.POST.get('quantity')
        company=request.POST.get('company')
        category=request.POST.get('category')
        desc=request.POST.get('desc')
        reg=products(pname=pname,ptype=ptype,price=price,warranty=warranty,photo=photo,quantity=quantity,company=company,
                     category=category,desc=desc)
        reg.save()
        prod.objects.filter(id=id).update(payment=False)
        # print("values uploaded")
        return redirect('adminhome')
    return render(request,'admin/addprod.html',{'pro':pro})




def restore(request):
    id=request.session['id']
    pro=company.objects.all()
    
    if request.method=="POST":
        
        
        pname=request.POST.get('pname')
        ptype=request.POST.get('ptype')
        quantity=request.POST.get('quantity')
        comp=request.POST.get('company')
        category=request.POST.get('category')
        adm=id
        reg=prod(pname=pname,ptype=ptype,quantity=quantity,company=comp,admin_id=adm,category=category)
        reg.save()
        # print("values uploaded")
        return redirect('adminhome')
    return render(request,'admin/restoreprod.html',{'pro':pro})



def vprod(request):
    pro=prod.objects.filter(payment=True)
    return render(request,'admin/viewprod.html',{'pro':pro})

def delprod(request,id):
    pro=prod.objects.filter(id=id)
    pro.delete()
    return redirect('adminhome')

def rejprod(request):
    pro=prod.objects.filter(reject=True)
    return render(request,'admin/rejectprod.html',{'pro':pro})

def cart(request):
    id=request.session['id']
    menu=prod.objects.filter(accept=True,reject=False,payment=False)
    global amount
    sum=0  
    amount=0     
    for i in menu:
            sum += float(i.price) * int(i.quantity)
            amount=sum
    return render(request,'admin/cart.html',{'menu':menu,'sum':sum,'amount':amount})



client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))

def payment(request):
    # id=request.session['id']
    global amount
    prod.objects.filter(accept=True).update(payment=True,accept=False)
    currency ="INR"
    api_key=RAZORPAY_API_KEY
    amt=int(amount)*100
    payment_order= client.order.create(dict(amount=amt,currency="INR",payment_capture=1))
    payment_order_id= payment_order['id'] 
    return render(request,'admin/payment.html',{'a':amount,'api_key':api_key,'order_id':payment_order_id})



def sattendance(request):
    pro=staff.objects.filter(accept=True)
    day=datetime.today().strftime('%y-%m-%d')
    
    if request.method == "POST":
        staffs = request.POST.getlist('staffs')  
        dates = request.POST.getlist('date')     
        statuses = request.POST.getlist('status')  
        
        for staff_id, date_val, status_val in zip(staffs, dates, statuses):
            reg = attendance(staffs=staff_id, date=date_val, status=status_val)
            reg.save()
        
        return redirect('adminhome')
    return render(request,'admin/attendance.html',{'pro':pro,'day':day})


def vattendance(request,id):
    sta=staff.objects.get(id=id)
    st=sta.staffname
    pro=attendance.objects.filter(staffs=st)
    return render(request,'admin/viewattendance.html',{'pro':pro,'sta':sta})


def stocks(request):
    pro=products.objects.all()
    return render(request,'admin/stocks.html',{'pro':pro})



def nullstocks(request):
    pro=products.objects.all()
    return render(request,'admin/nullstocks.html',{'pro':pro})

def delstock(request,id):
    pro=products.objects.filter(id=id)
    pro.delete()
    return redirect('adminhome')


def booked(request,id):
    pro=booking.objects.filter(customer=id,book=True) 
    return render(request,'admin/booked.html',{'pro':pro})


def custlist(request):
    pro=customer.objects.all() 
    return render(request,'admin/custlist.html',{'pro':pro})


def vcompl(request):
    pro=complaints.objects.all()
    return render(request,'admin/vcomplaint.html',{'pro':pro,'sum':sum})


def sendcomp(request,id):
    complaints.objects.filter(id=id).update(send=True)
    return redirect('adminhome')



def replycust(request,id):
    complaints.objects.filter(id=id).update(action=True)
    return redirect('adminhome')


def vreview(request,id):
    pro=products.objects.get(id=id)
    prof=prodrate.objects.filter(product=pro)
    return render(request,'admin/hreview.html',{'prof':prof})



client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))

def staffpayment(request,id):
    global amount
    sta=staff.objects.get(id=id)
    attendance.objects.filter(staffs=sta)
    pro=attendance.objects.filter(staffs=sta)
    i=0
    j=0
    sum=s=0
    amount=0      
    for r in pro:
        if (r.status == "Present"):
            i =i+1
            sum=i*1000
        if r.status == "Half Day":
            j=j+1
            s=j*500
        amount=sum+s
        r.delete()
    currency ="INR"
    api_key=RAZORPAY_API_KEY
    amt=int(amount) *100
    payment_order= client.order.create(dict(amount=amt,currency="INR",payment_capture=1))
    payment_order_id= payment_order['id'] 
    return render(request,'admin/payment.html',{'a':amount,'api_key':api_key,'order_id':payment_order_id,'sta':sta})


def salesreport(request):
    day=date.today()
    tod=datetime.today().strftime('%y-%m-%d')
    if request.method=="POST":
        startdate=request.POST.get('startdate')
        enddate=request.POST.get('enddate')
        sales=booking.objects.filter(date__range=[startdate,enddate])
        todaysale=booking.objects.filter(date=day)
        book=booking.objects.filter(payment=True)
        prods=prod.objects.filter(payment=True)

        total=0
        for b in book:
            total +=float(b.price)* int(b.quantity)

        totalprod=0
        for b in prods:
            totalprod +=float(b.total)

        sums=0
        for j in todaysale:
            sums +=int(j.price) * int(j.quantity)

        sales_data = defaultdict(int)
        quantity_data = defaultdict(int)

        for i in sales:
            sales_data[i.pname] += i.price
            quantity_data[i.pname] += i.quantity

        sales_list = [{'label': label, 'value': value, 'quantity': quantity} for label, value in sales_data.items() for label_q, quantity in quantity_data.items() if label_q == label]
        quantity_list = [{'label': label, 'quantity': quantity} for label, quantity in quantity_data.items()]

        sales_json = json.dumps(sales_list)
        quantity_json = json.dumps(quantity_list)

        avail_prod = products.objects.values('pname').annotate(total_quantity=Sum('quantity'), total_products=Count('pname'))
        purch_prod = prod.objects.filter(payment=True).values('pname').annotate(total_quantity=Sum('quantity'), total_products=Count('pname'))
        booked_prod = booking.objects.values('product__pname').annotate(total_quantity=Count('pname')).distinct().annotate(total_price=Sum(F('quantity') * F('price')))



        return render(request, 'admin/salesrep.html', {'startdate': startdate,'enddate': enddate,'todaysale':todaysale,'sales': sales,'sales_json': sales_json,
            'quantity_json': quantity_json,'sum': sum(sales_data.values())  ,'day':day,'sums':sums,'avail_prod':avail_prod,'booked_prod':booked_prod,
            'total':total,'purch_prod':purch_prod,'totalprod':totalprod,'today':tod    
            })
    
    return render(request,'admin/report.html',{'today':tod})
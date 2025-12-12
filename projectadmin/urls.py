from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('adminhome',views.adminhome,name="adminhome"),
    path('adminlog',views.adminlog,name="adminlog"),
    path('adminreg',views.adminreg,name="adminreg"),
    path('addprod<int:id>',views.addprod,name="addprod"),
    path('table',views.table,name="table"),
    path('restore',views.restore,name="restore"),
    path('vprod',views.vprod,name="vprod"),
    path('cart',views.cart,name="cart"),
    path('payment',views.payment,name="payment"),
    path('stocks',views.stocks,name="stocks"),
    path('vcompl',views.vcompl,name="vcompl"),
    path('nullstocks',views.nullstocks,name="nullstocks"),
    path('salesreport',views.salesreport,name="salesreport"),
    path('rejprod',views.rejprod,name="rejprod"),
    path('custlist',views.custlist,name="custlist"),

    path('comaccept<int:id>',views.comaccept,name="comaccept"),
    path('comreject<int:id>',views.comreject,name="comreject"),
    path('saccept<int:id>',views.saccept,name="saccept"),
    path('sreject<int:id>',views.sreject,name="sreject"),
    path('sattendance',views.sattendance,name="sattendance"),
    path('vattendance<int:id>',views.vattendance,name="vattendance"),
    path('delstock<int:id>',views.delstock,name="delstock"),
    path('sendcomp<int:id>',views.sendcomp,name="sendcomp"),
    path('replycust<int:id>',views.replycust,name="replycust"),
    path('vreview<int:id>',views.vreview,name="vreview"),
    path('staffpayment<int:id>',views.staffpayment,name="staffpayment"),
    path('delprod<int:id>',views.delprod,name="delprod"),
    path('booked<int:id>',views.booked,name="booked"),


]

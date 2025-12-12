from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('staffhome',views.staffhome,name="staffhome"),
    path('stafflog',views.stafflog,name="stafflog"),
    path('staffreg',views.staffreg,name="staffreg"),
    path('sprofile',views.sprofile,name="sprofile"),
    path('seditprof<int:id>',views.seditprof,name="seditprof"),
    path('satten',views.satten,name="satten"),
    path('prodbkd',views.prodbkd,name="prodbkd"),
    path('delivered<int:id>',views.delivered,name="delivered"),
]

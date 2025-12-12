from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('companyhome',views.companyhome,name="companyhome"),
    path('comlog',views.comlog,name="comlog"),
    path('comreg',views.comreg,name="comreg"),
    path('accept<int:id>',views.accept,name="accept"),
    path('reject<int:id>',views.reject,name="reject"),
    path('vprods',views.vprods,name="vprods"),
    path('accprods',views.accprods,name="accprods"),
    path('remove',views.remove,name="remove"),
    path('comprofile',views.comprofile,name="comprofile"),
    path('comeditprof<int:id>',views.comeditprof,name="comeditprof"),
    path('viewcopml',views.viewcopml,name="viewcopml"),
    path('reply<int:id>',views.reply,name="reply"),


]
#
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('signup', views.signup, name ='signup'),
    path('signin', views.signin, name ='signin'),
    path('signout', views.signout, name ='signout'),
    path('send-otp', views.send_otp, name='send_otp'),
    path('verify-otp', views.verify_otp, name='verify_otp'),
    
]
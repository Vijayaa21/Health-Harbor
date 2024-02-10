from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('signup', views.signup, name ='signup'),
    path('signin', views.signin, name ='signin'),
    path('signout', views.signout, name ='signout'),
    path('profile', views.profile, name = 'profile'),
    path('upload/', views.upload, name='upload_image'),
    path('getdiet', views.getdiet, name='get_diet'),

]
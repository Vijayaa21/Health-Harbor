from django.conf import settings
from django.urls import path
from home import views
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name = "home"),
    path('signup', views.signup, name ='signup'),
    path('signin', views.signin, name ='signin'),
    path('signout', views.signout, name ='signout'),
    path('profile', views.profile, name = 'profile'),
    path('upload/', views.upload, name='upload_image'),
    path('getdiet', views.getdiet, name='get_diet'),
    path('showdiet', views.showdiet, name='showdiet'),
    path('showMedical', views.showMedical, name='showMedical'),
    path('medicalreport/', views.medicalreport, name='medicalreport'),
    path('contact', views.contact, name='contact'), 

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
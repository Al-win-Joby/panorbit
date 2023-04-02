
from django.urls import path,include
from . import views 
from .views import *
urlpatterns = [
    #path('admin/', admin.site.urls),
    
    path('',views.landing,name="landing"),
    path('register/',registering.as_view(),name="registering"),
    path('registered',otp.as_view(),name="registered"),
    path('verifyotp/',signedup.as_view(),name="signedup"),

    path('home',views.home,name="home"),
    path('logout',views.logout1,name="logout"),
    path('login',views.login_view,name="login"),
    path('sendotp/',send_otpLogin.as_view(),name="sendotp"),
    path('verifyloginotp/',verifyloginotp.as_view(),name="verifyloginotp") ,
 

    path('sendotplogin',sendotplogin.as_view(),name="trialhome") 
    #path('home',home.as_view(),name="home")
    #path("send_otp",views.send_otp,name="send otp"),
]
       
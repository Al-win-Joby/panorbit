
from django.urls import path,include
from . import views 
from .views import *
urlpatterns = [
    
    #path('admin/', admin.site.urls),

    path('search',Search.as_view(),name="search"),
    path('searching',Searching.as_view(),name="searching"),
    path('<str:name>',GetCountry.as_view(),name="country_page")
    #path("send_otp",views.s end_otp,name="send otp"),
]
         
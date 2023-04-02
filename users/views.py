from django.shortcuts import render,redirect
from django.http import JsonResponse
from rest_framework.views import APIView
from .serializers import *
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail
import math, random
from django.views.decorators.cache import cache_control
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login,logout
from django.views.generic import TemplateView
# Create your views here. 
dic=0
otp=0


def landing(request):                               #show the landing signup page
    if request.user.is_authenticated:
        return redirect('/home')
    return render(request,'register.html') 
 
class registering(APIView):                       # Works when the user clicks the signup button

    
    def post(self,request):          
        Data=request.data 
        
        global dic
        global otp 
        dic=Data
        email=Data['email']
        phone=Data['phone'] 
        if CUser.objects.filter(email=email).exists():                        #Check whether existing user is present with same email
            
            return JsonResponse({ 'status':False, 'message':"Email exists"}) 
        
        if CUser.objects.filter(phone=phone).exists():                      #Check whether existing user is present with same number
            
            return JsonResponse({ 'status':False, 'message':"Phone number exists"}) 
                    
        print(email)
        o=generateOTP()
        print(o)
        otp = o

        request.session[email] = o                                          # Create a session with the given email and store otp 

        htmlgen = '<p>Your OTP is <strong>'+o+'</strong></p>'

        send_mail('OTP request',o,'panorbitxyz2023@gmail.com',[email], fail_silently=False, html_message=htmlgen)  #Email will be sent to the email
         
        return JsonResponse({'status':True,'otp':o}) 


class send_otpLogin(APIView):           
    def post(self,request):                         #Works when exisiting user tries to login
        Data=request.data
        email=Data['email'] 
        global otp          
        print("SENDOTP")
        request.session['email']=email          
        
        if not CUser.objects.filter(email=email).exists():
            #messages.info(request,"Email exist") 
            return JsonResponse({ 'status':False, 'message':"Email does not exists"}) 
        else:
            o=generateOTP()
            print(o)
            otp=o   
            htmlgen = '<p>Your OTP is <strong>'+o+'</strong></p>'

            send_mail('OTP request',o,'panorbitxyz2023@gmail.com',[email], fail_silently=False, html_message=htmlgen)         
            return JsonResponse({'status':True}) 
        

class verifyloginotp(APIView): 
    def post(self,request):         # Validate the otp and makes user loggedin
        global otp
        Data=request.data
        num=Data['inp1']+Data['inp2']+Data['inp3']+Data['inp4']
    
        
        email=request.session['email']
        realotp = otp
        print(realotp)
        if realotp!=num:

            return JsonResponse({ 'status':False, 'message':"Invalid OTP"}) 
        else:
            user=CUser.objects.get(email=email)

            #user=authenticate(request,email=email)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')   
            del request.session['email']
            return JsonResponse({'status':True})
         
 
class signedup(APIView):           
    def post(self,request):             # Function to validate OTP  and create user while signup
       
        Data=request.data
        num=Data['inp1']+Data['inp2']+Data['inp3']+Data['inp4']
        email=dic['email']              
        realotp=request.session[email]

        if realotp!=num:                                            

            return JsonResponse({ 'status':False, 'message':"Invalid OTP"}) 
        else:                                                                      # Works when entered otp is correct
            user=CUser.objects.create_user(first_name=dic['first_name'],last_name=dic['last_name'],
                                      gender=dic['gender'],phone=dic['phone'],email=dic['email'])

            login(request, user, backend='django.contrib.auth.backends.ModelBackend') # User gets logged in
            del request.session[email]
            return JsonResponse({'status':True}) 
 
class sendotplogin(TemplateView):
    
    template_name = 'loginotp.html' 
   
  
class otp(TemplateView):
    
    template_name = 'otp.html' 
  

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return  render(request,'home.html')  

def logout1(request):
    
    logout(request)
    return redirect('login')


def login_view(request):
    return render(request,'login.html')

############################################################################################### 

def generateOTP() :                             #Function to generate OTP
     digits = "0123456789"
     OTP = ""
     for i in range(4) :
         OTP += digits[math.floor(random.random() * 10)] 
     return OTP  

def send_otp(request):
     email=request.GET.get("email") 
     print(email)
     o=generateOTP()
     htmlgen = '<p>Your OTP is <strong>o</strong></p>'
     send_mail('OTP request',o,'<your gmail id>',[email], fail_silently=False, html_message=htmlgen)
     return HttpResponse(o)
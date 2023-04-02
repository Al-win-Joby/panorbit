from django.shortcuts import render,redirect
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.response import Response 


# Create your views here.

class Search(APIView):                             #Works when search button is clicked
    renderer_classes = [TemplateHTMLRenderer]
       
    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('/login')
        Data=request.data 
        
        Data1 = Data['searched_data'].capitalize()          #To make the first letter to uppercase as datas are store accordingly
        
        if City.objects.filter(Name=Data1).exists():        #Checks if user entered a city name

            citi=City.objects.get(Name=Data1)
            print(citi.CountryCode)
            
            country=Country.objects.get(Name=citi.CountryCode)
            serializer = CitySerializer(citi,many=False)
            Cserializer= CountrySerializer(country,many=False)            
            
            return Response({'City':serializer.data,'Country':Cserializer.data},template_name='city.html')
    
        elif CountryLanguage.objects.filter(Language=Data1).exists():           #Checks if user entered a country language
            language=CountryLanguage.objects.filter(Language=Data1)

            serializer= LanguageSerializer(language,many=True)
            
            l=len(serializer.data)
            
            dict_data={x:serializer.data[x] for x in range(l)}
            
            print(dict_data)
            return Response({'dict_data':dict_data},template_name='language.html')
             

        elif Country.objects.filter(Name=Data1).exists():                   #Checks if user entered a Country name
            country=Country.objects.get(Name=Data1)
            serializer=CountryFullSerializer(country,many=False)
            print(serializer.data)
            return Response(serializer.data,template_name='country.html')
        else: 
            return redirect('/home')
        

class Searching(APIView):

    def get(self,request):                                                   #Works when value is typed in the search bar
        if not request.user.is_authenticated:
            return redirect('/login')
        query=request.GET.get('dataa')
        
        countries = Country.objects.filter(Name__icontains=query)
        countryserialized=CountrySerializer(countries,many=True)
        
        languages = CountryLanguage.objects.filter(Language__icontains=query).values('Language').distinct()
        languageserilazer=LanguageNameSerializer(languages,many=True)

        cities = City.objects.filter(Name__icontains=query)
        citiserializer= CityNameSerializer(cities,many=True)
        
        dic={}
        
        l=len(countryserialized.data)
        
        for i in range(l):
            dic[i]=countryserialized.data[i]

        
        print(languageserilazer.data)    

        l1=len(languageserilazer.data)
        for j in range(l1):
            dic[l+j]=languageserilazer.data[j]

        l2=len(citiserializer.data)
        for z in range(l2):                                         
            dic[l+l1+z]=citiserializer.data[z]

        print(dic)                                          
        return Response({'dic':dic})
       

class GetCountry(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    def get(self,request,name):                                            #Works when a country name is clicked in city and language pages
        if not request.user.is_authenticated:
            return redirect('/login')   
        print(name)
        country=Country.objects.get(Name=name)
        serializer=CountryFullSerializer(country,many=False)
        print(serializer.data)
        return Response(serializer.data,template_name='country.html')


 
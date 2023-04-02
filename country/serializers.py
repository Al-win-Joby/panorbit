from rest_framework import serializers,renderers

from .models import *
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class LanguageSerializer(serializers.ModelSerializer):
    country_name = serializers.SerializerMethodField()
    class Meta:
        model = CountryLanguage
        fields = ('id','CountryCode','Language','IsOfficial','Percentage','country_name')
    
    def get_country_name(self, obj):
        return obj.CountryCode.Name

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('Name',)    

class LanguageNameSerializer(serializers.ModelSerializer):
    Name = serializers.CharField(source='Language')
    class Meta:
        model = CountryLanguage
        fields = ('Name',)


class CityNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('Name',)


class CountryFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'  

class MySerializer(serializers.Serializer):
    # Define your serializer fields here

    class Meta:
        # Set the renderer classes here
        renderer_classes = [renderers.TemplateHTMLRenderer, renderers.JSONRenderer]
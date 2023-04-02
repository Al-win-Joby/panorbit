from rest_framework import serializers
from .models import CUser 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CUser
        fields='__all__'
        #fields = ('first_name','last_name','email','phone')

    def create(self,validated_data):
        print("yes")
        instance = self.Meta.model(**validated_data) 
        instance.save()
        return instance 
              
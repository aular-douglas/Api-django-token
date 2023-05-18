from django.contrib.auth import get_user_model 
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    model = get_user_model()
    fields = ['email', 'password', 'name']
    extra_kwargs ={'password': {'write_only':True}}
    
def create(self, validate_data):
    return get_user_model().objects.create_user(**validate_data)

def update(self, instance, validated_data):
    password = validated_data.pop('password', None)
    user = super().update(instance, validated_data)
    
    if password:
        user.set_password(password)
        user.save() 
        
    return  user       
    
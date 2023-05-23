from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = get_user_model()
        fields = ['email', 'password', 'name']
        extra_kwargs ={'password': {'write_only':True}}
    
        def create(self, validate_data):
            User = get_user_model()
            
            return User.objects.create_user(**validate_data)

        def update(self, instance, validated_data):
            password = validated_data.pop('password', None)
            user = super().update(instance, validated_data)
            
            if password:
                user.set_password(password)
                user.save() 
                
            return  user       

class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})
    
    def validate(self, data):
        print(data)
        email = data.get('email')
        password = data.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )   
        
        if not user:
            raise serializers.ValidationError('No se pudo autenticar', code='authorization')
        
        data['user'] = user
        return data
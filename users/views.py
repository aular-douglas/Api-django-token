from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken 
from users.serializers import UserSerializer, AuthTokenSerializer
from users.models import User
from django.contrib.auth.hashers import make_password 

# Create your views here.

class CreateUserView(generics.CreateAPIView):
    queryset= User.objects.all()
    serializer_class = UserSerializer
    
    def create(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password'])
    
        return super().create(request, *args, **kwargs)

class listUsersView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
class RetreiveUpdateUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        return self.request.user
    
class CreateTokenView(ObtainAuthToken):
    """Vista para Crear un token"""
    serializer_class = AuthTokenSerializer
    
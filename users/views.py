from rest_framework import generics
from users.serializers import UserSerializer
from users.models import User

# Create your views here.

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class listUsersView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.object.all()
    
    '''def get_queryset(self):
        return User.objects.all()'''
    
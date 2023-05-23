from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from activities.models import ActivityList, ActivityItem
from activities.serializers import ActivityListSerializer

class ActivityListViewSet(ModelViewSet):
    queryset = ActivityList.objects.all()
    serializer_class = ActivityListSerializer
    Permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

def get_queryset(self):
    return self.queryset.filter(owner=self.request.user)

def perform_create(self, serializer):
    user = self.request.user
    serializer.save(owner=user)
    

    

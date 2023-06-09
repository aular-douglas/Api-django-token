from django.urls import path, include
from rest_framework.routers import DefaultRouter

from activities.views import ActivityListViewSet

router = DefaultRouter()
router.register(r'lists', ActivityListViewSet, basename='list')

urlpatterns = [
    path('', include(router.urls))
]

from rest_framework import serializers 
from activities.models import ActivityItem, ActivityList

class ActivityListSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    status = serializers.ReadOnlyField()
    item_count = serializers.ReadOnlyField()
    
    class Meta:
        model = ActivityList
        fields = '__all__'
        
    def to_representation(self, instance):
        representation = super(ActivityListSerializer, self).to_representation(instance)
        representation['date_created'] = instance.date_created.astimezone().strftime("%Y-%m-%d %H:%M")    
        return representation
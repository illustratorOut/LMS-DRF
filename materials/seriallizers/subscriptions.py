from rest_framework import serializers
from materials.models import Subscriptions


class SubscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriptions
        fields = ('user', 'course', 'status')

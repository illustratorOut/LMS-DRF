from rest_framework import serializers
from users.models import User
from users.seriallizers.payment import PaymentSerializer


class UserSerializer(serializers.ModelSerializer):
    payment_history = PaymentSerializer(source='payment_set', many=True)

    class Meta:
        model = User
        fields = ('email', 'payment_history')


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'last_name',)

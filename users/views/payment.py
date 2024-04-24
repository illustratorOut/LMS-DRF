from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView

from users.models import Payment
from users.seriallizers.payment import PaymentSerializer


class PaymentListView(ListAPIView):
    ''' Отображение списка сущностей '''
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('method', 'course', 'lesson', 'date_payment')

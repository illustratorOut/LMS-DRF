from rest_framework.generics import ListAPIView, CreateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from materials.models import Subscriptions, Course
from materials.seriallizers.subscriptions import SubscriptionsSerializer
from materials.services import Stripe_API
from users.models import Payment


class SubscriptionsListView(ListAPIView):
    '''Отображение списка сущностей'''
    queryset = Subscriptions.objects.all()
    serializer_class = SubscriptionsSerializer
    permission_classes = [IsAuthenticated]


class SubscriptionsCreateView(CreateAPIView):
    '''Создание сущности'''
    queryset = Subscriptions.objects.all()
    serializer_class = SubscriptionsSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data['course']
        course_item = get_object_or_404(Course, pk=course_id)

        subs_item = Subscriptions.objects.filter(user=user).filter(course=course_item)

        if subs_item.exists():
            subs_item.delete()
            message = 'подписка удалена'
        else:
            Subscriptions.objects.create(user=user, course=course_item, status=True)
            message = 'подписка добавлена'
        return Response({"message": message})


class StripeAPIView(APIView):
    '''Создание сущности Stripe'''
    permission_classes = [IsAuthenticated]

    def post(self, *args, **kwargs):
        course_id = kwargs.get('pk')
        payment = get_object_or_404(Payment, course=course_id)
        stripe_api = Stripe_API()

        if payment.price_id is None or payment.product_id is None:
            price = stripe_api.create_product(payment.course.name, payment.amount)
            payment.price_id = price['id']
            payment.product_id = price['product']
            payment.save()
        session = stripe_api.create_session(payment.price_id)
        payment.session_id = session.get('id')
        payment.save()

        return Response({'url': session.url})


class StripePaymentStatusAPIView(APIView):
    '''Статус платежа Stripe'''
    permission_classes = [IsAuthenticated]

    def post(self, *args, **kwargs):
        course_id = kwargs.get('pk')
        stripe_api = Stripe_API()
        payment = get_object_or_404(Payment, course=course_id)
        res = stripe_api.retrieve_session(payment.session_id)
        payment_status = res.get('payment_status')

        payment.payment_status = payment_status
        payment.save()

        return Response({'payment_status': payment_status})

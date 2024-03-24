from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from materials.models import Subscriptions, Course
from materials.paginators import CustomPagination
from materials.seriallizers.subscriptions import SubscriptionsSerializer


class SubscriptionsListView(ListAPIView):
    ''' Отображение списка сущностей '''
    queryset = Subscriptions.objects.all()
    serializer_class = SubscriptionsSerializer
    permission_classes = [IsAuthenticated]


class SubscriptionsCreateView(CreateAPIView):
    ''' Создание сущности '''
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

import datetime

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from materials.models import Course, Subscriptions
from materials.paginators import CustomPagination
from materials.permissions import IsOwner, IsModerator
from materials.seriallizers.course import CourseSerializer
from materials.tasks import send_mail_update_course
from django.utils import timezone


class CourseViewSet(viewsets.ModelViewSet):
    '''Отображение сущностей RESTful API'''
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        '''При создании obj присваиваем автора(user)'''
        new_dog = serializer.save()
        new_dog.owner = self.request.user
        new_dog.save()

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, IsModerator | IsOwner]
        return [permission() for permission in permission_classes]

    def perform_update(self, serializer):
        '''Отправка сообщений при обновлении курса'''
        update_course = serializer.save()
        subscribers = Subscriptions.objects.filter(course=update_course.pk).values()
        course = Course.objects.filter(pk=update_course.pk)[0]

        if subscribers and course.date_update > timezone.now() + timezone.timedelta(hours=4):
            for subscriber in subscribers:
                send_mail_update_course.delay(subscriber['user_id'], update_course.pk)

        update_course.date_update = timezone.now()
        update_course.save()

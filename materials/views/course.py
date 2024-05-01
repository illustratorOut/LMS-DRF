import json

from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from materials.models import Course, Subscriptions
from materials.paginators import CustomPagination
from materials.permissions import IsOwner, IsModerator
from materials.seriallizers.course import CourseSerializer
from materials.tasks import send_mail_update_course


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
        print(update_course)
        # subscribers = get_object_or_404(Subscriptions, course=update_course.pk)
        subscribers = Subscriptions.objects.filter(course=update_course.pk).values()

        send_mail_update_course.delay(subscribers, update_course)

        update_course.save()

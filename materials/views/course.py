from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from materials.models import Course
from materials.paginators import CustomPagination
from materials.permissions import IsOwner, IsModerator
from materials.seriallizers.course import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    ''' Отображение сущностей RESTful API'''
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        ''' При создании obj присваиваем автора(user) '''
        new_dog = serializer.save()
        new_dog.owner = self.request.user
        new_dog.save()

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, IsModerator | IsOwner]
        return [permission() for permission in permission_classes]

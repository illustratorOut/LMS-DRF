import datetime

from rest_framework.generics import RetrieveAPIView, DestroyAPIView, ListAPIView, UpdateAPIView, CreateAPIView, \
    get_object_or_404
from rest_framework.permissions import IsAuthenticated

from materials.models import Lesson, Course
from materials.paginators import CustomPagination
from materials.permissions import IsModerator, IsOwner
from materials.seriallizers.lesson import LessonSerializer, LessonCreateSerializer


class LessonDetailView(RetrieveAPIView):
    '''Отображение одной сущности'''
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonListView(ListAPIView):
    '''Отображение списка сущностей'''
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination


class LessonCreateView(CreateAPIView):
    '''Создание сущности'''
    queryset = Lesson.objects.all()
    serializer_class = LessonCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        '''При создании obj присваиваем автора(user)'''
        new_dog = serializer.save()
        new_dog.owner = self.request.user
        new_dog.save()


class LessonUpdateView(UpdateAPIView):
    '''Редактирование (обновление) сущности'''
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]

    def perform_update(self, serializer):
        update_lesson = serializer.save()
        course = get_object_or_404(Course, pk=update_lesson.linl_course)
        course.update(date_update=datetime.datetime.now())
        update_lesson.save()


class LessonDeleteView(DestroyAPIView):
    '''Удаление сущности'''
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwner]

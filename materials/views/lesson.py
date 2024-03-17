from rest_framework.generics import RetrieveAPIView, DestroyAPIView, ListAPIView, UpdateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from materials.models import Lesson
from materials.permissions import IsModerator, IsOwner
from materials.seriallizers.lesson import LessonSerializer


class LessonDetailView(RetrieveAPIView):
    ''' Отображение одной сущности '''
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonListView(ListAPIView):
    ''' Отображение списка сущностей '''
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]


class LessonCreateView(CreateAPIView):
    ''' Создание сущности '''
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        ''' При создании obj присваиваем автора(user) '''
        new_dog = serializer.save()
        new_dog.owner = self.request.user
        new_dog.save()


class LessonUpdateView(UpdateAPIView):
    '''  Редактирование сущности '''
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonDeleteView(DestroyAPIView):
    ''' Удаление сущности '''
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwner]

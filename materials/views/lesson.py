from rest_framework.generics import RetrieveAPIView, DestroyAPIView, ListAPIView, UpdateAPIView, CreateAPIView

from materials.models import Lesson
from materials.seriallizers.lesson import LessonSerializer


class LessonDetailView(RetrieveAPIView):
    ''' Отображение одной сущности '''
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonListView(ListAPIView):
    ''' Отображение списка сущностей '''
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonCreateView(CreateAPIView):
    ''' Создание сущности '''
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonUpdateView(UpdateAPIView):
    '''  Редактирование сущности '''
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDeleteView(DestroyAPIView):
    ''' Удаление сущности '''
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

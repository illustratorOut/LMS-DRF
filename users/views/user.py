from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from users.models import User
from users.seriallizers.user import UserSerializer


class UserDetailView(RetrieveAPIView):
    ''' Отображение одной сущности '''
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserListView(ListAPIView):
    ''' Отображение списка сущностей '''
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateView(CreateAPIView):
    ''' Создание сущности '''
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateView(UpdateAPIView):
    '''  Редактирование сущности '''
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDeleteView(DestroyAPIView):
    ''' Удаление сущности '''
    queryset = User.objects.all()
    serializer_class = UserSerializer

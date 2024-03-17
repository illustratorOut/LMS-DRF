from rest_framework.permissions import AllowAny
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.permissions import IsUserProfile
from users.seriallizers.user import UserSerializer, UserDetailSerializer


class LoginListView(ListAPIView):
    ''' Отображение авторизации '''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class RegisterationListView(ListAPIView):
    ''' Отображение регистрации '''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserDetailView(RetrieveAPIView):
    ''' Отображение одной сущности '''
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]


class UserListView(ListAPIView):
    ''' Отображение списка сущностей '''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserCreateView(CreateAPIView):
    ''' Создание сущности '''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserUpdateView(UpdateAPIView):
    '''  Редактирование сущности '''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsUserProfile]


class UserDeleteView(DestroyAPIView):
    ''' Удаление сущности '''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

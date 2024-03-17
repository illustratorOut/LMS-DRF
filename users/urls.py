from django.urls import path

from users.apps import UsersConfig
from users.views.payment import PaymentListView
from users.views.user import UserListView, UserDetailView, UserUpdateView, UserCreateView, UserDeleteView, \
    LoginListView, RegisterationListView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = UsersConfig.name

urlpatterns = [
    # авторизации и регистрации
    path('login/', LoginListView.as_view()),
    path('registration/', RegisterationListView.as_view()),

    # User
    path('', UserListView.as_view()),
    path('<int:pk>/', UserDetailView.as_view()),
    path('create/', UserCreateView.as_view()),
    path('update/<int:pk>/', UserUpdateView.as_view()),
    path('delete/<int:pk>/', UserDeleteView.as_view()),

    # Payment
    path('payment/', PaymentListView.as_view()),

    # Token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

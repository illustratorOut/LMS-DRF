from django.urls import path

from users.apps import UsersConfig
from users.views.payment import PaymentListView
from users.views.user import UserListView, UserDetailView, UserUpdateView, UserCreateView, UserDeleteView

app_name = UsersConfig.name

urlpatterns = [
    path('', UserListView.as_view()),
    path('<int:pk>/', UserDetailView.as_view()),
    path('<int:pk>/update/', UserUpdateView.as_view()),
    path('create/', UserCreateView.as_view()),
    path('<int:pk>/delete/', UserDeleteView.as_view()),

    # Payment
    path('payment/', PaymentListView.as_view()),
]

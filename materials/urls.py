from django.urls import path
from rest_framework.routers import DefaultRouter

from materials.apps import MaterialsConfig
from materials.views.course import CourseViewSet

from materials.views.lesson import LessonListView, LessonDetailView, LessonUpdateView, LessonCreateView, \
    LessonDeleteView

app_name = MaterialsConfig.name

urlpatterns = [
    path('', LessonListView.as_view()),
    path('<int:pk>/', LessonDetailView.as_view()),
    path('create/', LessonCreateView.as_view()),
    path('update/<int:pk>/', LessonUpdateView.as_view()),
    path('delete/<int:pk>/', LessonDeleteView.as_view()),
]

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='Course')

urlpatterns += router.urls

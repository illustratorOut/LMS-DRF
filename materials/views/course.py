from rest_framework import viewsets

from materials.models import Course
from materials.seriallizers.course import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

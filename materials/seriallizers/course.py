from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from materials.models import Course
from materials.seriallizers.lesson import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    count_lessons = SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_count_lessons(self, instance):
        if instance.lesson_set.all():
            return instance.lesson_set.all().count()
        return 0

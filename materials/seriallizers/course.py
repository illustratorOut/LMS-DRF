from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from materials.models import Course
from materials.seriallizers.lesson import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    count_lessons = SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)
    subscriptions = SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_count_lessons(self, instance):
        if instance.lesson_set.all():
            return instance.lesson_set.all().count()
        return 0

    def get_subscriptions(self, instance):
        if instance.subscriptions_set.all():
            return True
        else:
            return False

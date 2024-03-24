from rest_framework import serializers

from materials.models import Lesson
from materials.validators import LinkVideoValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class LessonCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [LinkVideoValidator(field='link_video')]

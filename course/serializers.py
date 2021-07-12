from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['id', 'course_name', 'author', 'created_at', 'price','enrolled']
        depth = 1
        exclude = ()


from rest_framework import serializers
from course.models import Course, Wishlist


class CourseSerializer(serializers.ModelSerializer):	
    class Meta:
        model = Course
        field = '__all__'
        depth = 1
        exclude = ()


class WishlistSerializer(serializers.ModelSerializer):	
    class Meta:
        model = Wishlist
        field = '__all__'
        depth = 1
        exclude = ()
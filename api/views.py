from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from .serializers import CourseSerializer
from course.models import Course

# Create your views here.
class ListCourseAPIView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CreateCourseAPIView(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class UpdateCourseAPIView(UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class DeleteCourseAPIView(DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
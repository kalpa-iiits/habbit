from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import CourseSerializer
from .models import Course
from rest_framework import permissions
from .permissions import IsOwner


class CourseListAPIView(ListCreateAPIView):
    """
    Class to retrn course list

    Attributes
    ---------------------------------------
    Course  data
        
    Methods
    --------------------------------------
    GET method to get all set of courses
    POST method to create a new course

    Return
    --------------------------------------
    Course list
    
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class CourseDetailAPIView(RetrieveUpdateDestroyAPIView):

    """
    Class to retrn a single course

    Attributes
    ---------------------------------------
    Course attrs
        
    Methods
    --------------------------------------
    GET method to het single course data

    Return
    --------------------------------------
    Single course serialized data
    
    """

    serializer_class = CourseSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    queryset = Course.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

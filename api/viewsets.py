from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from .serializers import CourseSerializer, WishlistSerializer
from course.models import Course, Wishlist
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.
class ListCourseAPIView(ListAPIView):
	permission_classes = (IsAuthenticated,)
	queryset=Course.objects.all()
	serializer_class=CourseSerializer

class CreateCourseAPIView(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class UpdateCourseAPIView(UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class DeleteCourseAPIView(DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class ListWishlistAPIView(ListAPIView):
	permission_classes = (IsAuthenticated,)
	queryset = Wishlist.objects.all()
	serializer_class = WishlistSerializer

class CreateWishlistAPIView(CreateAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer

class UpdateWishlistAPIView(UpdateAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer

class DeleteWishlistAPIView(DestroyAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
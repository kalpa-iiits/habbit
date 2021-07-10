from django.shortcuts import render
from .serializers import CourseSerializer, WishlistSerializer
from course.models import Course, Wishlist
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from django.http import Http404



class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class CourseList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    authentication_classess = [TokenAuthentication]

    def get(self, request, format=None):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

class CourseDetail(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    authentication_classess = [TokenAuthentication]

    def get_object(self,pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        course = self.get_object(pk)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        course = self.get_object(pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WishlistList(APIView):
    permission_classes = (IsOwnerOrReadOnly,)
    authentication_classess = [TokenAuthentication]

    def get(self, request, format=None):
        wishlist = Wishlist.objects.all()
        serializer = WishlistSerializer(wishlist, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WishlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    


class WishlistDetail(APIView):
    permission_classes = (IsOwnerOrReadOnly, IsAdminOrReadOnly,)
    authentication_classess = [TokenAuthentication]

    def get_object(self,pk):
        try:
            return Wishlist.objects.get(pk=pk)
        except Wishlist.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        wishlist = self.get_object(pk)
        serializer = WishlistSerializer(wishlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        wishlist = self.get_object(pk)
        wishlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

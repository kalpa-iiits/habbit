from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import WishlistSerializer
from .models import Wishlist
from rest_framework import permissions
from .permissions import IsOwner


class WishlistListAPIView(ListCreateAPIView):
    serializer_class = WishlistSerializer
    queryset = Wishlist.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class WishlistDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = WishlistSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    queryset = Wishlist.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

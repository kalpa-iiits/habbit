from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import WishlistSerializer
from .models import Wishlist
from rest_framework import permissions
from .permissions import IsOwner


class WishlistListAPIView(ListCreateAPIView):
    """
    Class to obtain all the wishlist 

    Attributes
    ---------------------------------------
    Wishlist data
        
    Methods
    --------------------------------------
    Post method to create data
    Get method to obtain wishlist

    Sends email to user email for user verification,
    The mail contains a JSW token

    Return
    --------------------------------------
    Serialized wishlist data
    
    """
    serializer_class = WishlistSerializer
    queryset = Wishlist.objects.all()
   

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class WishlistDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    Class to retrn a single wishlist

    Attributes
    ---------------------------------------
    Wishlist data
        
    Methods
    --------------------------------------
    GET method to het single wishlist data

    Return
    --------------------------------------
    Single wishlist serialized data
    
    """
    serializer_class = WishlistSerializer
    queryset = Wishlist.objects.all()
    lookup_field = "id"

    

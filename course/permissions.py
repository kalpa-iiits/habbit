'''
Module defining permisiions

'''
from rest_framework import permissions


class IsOwner(permissions.BasePermission):


    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

    """
    Class to define user prmissions

    Methods
    --------------------------------------
    Defines wether a user class has permission or not

    Return
    --------------------------------------
    User accessibility
    
    """
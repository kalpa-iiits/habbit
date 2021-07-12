'''
Module that defines the structre of wishlist

'''
from django.db import models
from authentication.models import User
from course.models import Course


# Create your models here.

class Wishlist(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True, related_name='user_wishlist')
    course_name = models.ManyToManyField(Course, blank=True, related_name='course_in_wishlist')

    def __str__(self):
        return str(self.id)
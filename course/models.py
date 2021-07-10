from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User



class Course(models.Model):
    course_name=models.CharField(max_length=250)
    author_name=models.CharField(max_length=250)
    date=models.DateTimeField(auto_now=False, auto_now_add=True)
    price=models.IntegerField()
    enrolled=models.ManyToManyField(User, blank=True)
   
    def __str__(self):
        return str(self.id)


class Wishlist(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    course_name = models.ManyToManyField(Course, blank=True)

    def __str__(self):
        return str(self.id)
   
  

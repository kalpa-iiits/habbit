'''
Module defining permisiions

'''
from django.db import models
from authentication.models import User

#Creating course model

class Course(models.Model):
    course_name=models.CharField(max_length=250)
    author=models.ForeignKey(to=User, on_delete=models.CASCADE,null=True,blank=True, related_name='author')
    created_at=models.DateTimeField(auto_now=False, auto_now_add=True)
    price=models.IntegerField()
    enrolled=models.ManyToManyField(to=User, blank=True, related_name='enrolled')
   
    def __str__(self):
        return str(self.id)
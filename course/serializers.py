"""
Module to serialze course objects and querysets 

"""
from rest_framework import serializers
from .models import Course




class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = ['id', 'course_name', 'author', 'created_at', 'price','enrolled']
		depth = 1
		exclude = ()

        
        
        
	"""
		Class to serialize Course data 
		
		Attributes
		-------------------------------
		Attrbuites are attained from Course model

		-------------------------------
		Serialized data of Course

	"""
    


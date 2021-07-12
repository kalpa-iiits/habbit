"""
Module to serialze wishlist objects and querysets 

"""
from rest_framework import serializers
from .models import Wishlist


class WishlistSerializer(serializers.ModelSerializer):
	class Meta:
		"""
	    Class to serialize Wishlist data 

	    Attributes
	    -------------------------------
	    Attrbuites are attained from Wishlist model

	    Return
	    -------------------------------
	    Serialized data of Wishlist
	    
	    """
		model = Wishlist
		fields = ['user', 'course_name']
		exclude = ()
		depth = 1

        

	

    

from django.contrib import admin
from .models import Course, Wishlist, Profile

# Register your models here.
admin.site.register(Course)
admin.site.register(Wishlist)
admin.site.register(Profile)
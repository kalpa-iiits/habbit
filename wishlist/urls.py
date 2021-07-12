'''
Module containing url of whishlist app

'''
from django.urls import path
from . import views


urlpatterns = [
    path('', views.WishlistListAPIView.as_view(), name="wishlist"),
    path('<int:id>', views.WishlistDetailAPIView.as_view(), name="wishlist_product_detail"),
]

from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import CourseDetail, CourseList, WishlistList, WishlistDetail
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('gettoken/', obtain_auth_token, name='api_token_auth'),
    path('course/', CourseList.as_view(), name="course_list" ),
    path("course/<int:pk>/", CourseDetail.as_view(), name="course_detail"),
    path('wishlist/', WishlistList.as_view(), name="wishlist_list" ),
    path("wishlist/<int:pk>/", WishlistDetail.as_view(), name="wishlist_detail"),
]
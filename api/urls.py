from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import ListCourseAPIView, CreateCourseAPIView, DeleteCourseAPIView,UpdateCourseAPIView
from .views import ListWishlistAPIView, UpdateWishlistAPIView, CreateWishlistAPIView, DeleteWishlistAPIView
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path("course/",ListCourseAPIView.as_view(),name="course_list"),
    path("course/create/", CreateCourseAPIView.as_view(),name="course_create"),
    path("course/update/<int:pk>/",UpdateCourseAPIView.as_view(),name="update_course"),
    path("course/delete/<int:pk>/",DeleteCourseAPIView.as_view(),name="delete_course"),
    path("wishlist/",ListWishlistAPIView.as_view(),name="course_list"),
    path("wishlist/create/", CreateWishlistAPIView.as_view(),name="course_create"),
    path("wishlist/update/<int:pk>/",UpdateWishlistAPIView.as_view(),name="update_course"),
    path("wishlist/delete/<int:pk>/",DeleteWishlistAPIView.as_view(),name="delete_course"),
    path('gettoken/', obtain_auth_token, name='api_token_auth'),
]
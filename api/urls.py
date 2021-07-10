from django.urls import path
from . import views

urlpatterns = [
    path("course/",views.ListCourseAPIView.as_view(),name="course_list"),
    path("course/create/", views.CreateCourseAPIView.as_view(),name="course_create"),
    path("course/update/<int:pk>/",views.UpdateCourseAPIView.as_view(),name="update_course"),
    path("course/delete/<int:pk>/",views.DeleteCourseAPIView.as_view(),name="delete_course"),
    path("wishlist/",views.ListWishlistAPIView.as_view(),name="course_list"),
    path("wishlist/create/", views.CreateWishlistAPIView.as_view(),name="course_create"),
    path("wishlist/update/<int:pk>/",views.UpdateWishlistAPIView.as_view(),name="update_course"),
    path("wishlist/delete/<int:pk>/",views.DeleteWishlistAPIView.as_view(),name="delete_course"),
]
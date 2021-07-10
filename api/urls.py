from django.urls import path
from . import views

urlpatterns = [
    path("",views.ListCourseAPIView.as_view(),name="course_list"),
    path("create/", views.CreateCourseAPIView.as_view(),name="course_create"),
    path("update/<int:pk>/",views.UpdateCourseAPIView.as_view(),name="update_course"),
    path("delete/<int:pk>/",views.DeleteCourseAPIView.as_view(),name="delete_course")
]
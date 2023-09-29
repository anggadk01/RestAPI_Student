from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="/"),
    path('student-view/<str:pk>/', views.studentView, name="studentview"),
    path('student-add/', views.studentAdd, name="studentadd"), #post
    path('student-update/<str:pk>/', views.studentUpdate, name="studentupdate"), #post update
    path('student-delete/<str:pk>/', views.studentDelete, name="studentdelete"), # delete
]


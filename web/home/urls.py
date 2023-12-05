from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about, name='about'),
    path('course/', views.course, name='course'),
    path('course/<int:pk>/lesson', views.course_list, name='course_list'),
    path('courses/<int:pk>/lesson/videos', views.learn, name='learn'),
    path('list_admin/', views.list_admin, name='list_admin'),
    path('courses/<int:pk>', views.course_detail, name='course_detail'),
    path('courses/videos/<int:pk>', views.video_detail, name='video_detail'),
    path('edit_course/<int:pk>', views.edit_course, name='edit_course'),
    path('add/', views.add_course, name='add_course'),
    path('join_course/<int:pk>/', views.join_course, name='join_course'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about, name='about'),
    path('course/', views.course, name='course'),
    path('learn/', views.learn, name='learn'),
    path('list', views.course_list, name='course_list'),
    path('add/', views.add_course, name='add_course'),

]

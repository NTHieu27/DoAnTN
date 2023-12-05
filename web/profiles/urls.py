from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test, name='test'),
    path('list-user/', views.update_user, name='update_user'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('edit-profile', views.edit_profile, name='edit_profile'),
    path('list-user/<int:pk>', views.user_detail, name='user_detail'),
]

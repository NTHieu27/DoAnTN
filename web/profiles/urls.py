from django.urls import path
from . import views

urlpatterns = [
    path('update_user/', views.update_user, name='update_user')
]

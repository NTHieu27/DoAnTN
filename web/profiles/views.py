from django.shortcuts import render
from django.contrib.auth.views import LoginView


# Create your views here.

def update_user(request):
    return render(request, "update_user.html", {})

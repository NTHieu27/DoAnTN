from django.forms import CharField
from django.shortcuts import render
from .models import Course
from .forms import CourseForm


def index(request):
    return render(request, 'page/home.html', {
        'nav': "home"
    })


def about(request):
    return render(request, 'page/about.html', {
        'nav': "about"
    })


def course(request):
    object_list = Course.objects.all()
    return render(request, 'page/course.html', {
        'object_list': object_list,
    })


def learn(request):
    courses = Course.objects.all()
    return render(request, 'page/learn.html', {'courses': courses})


def course_list(request):
    courses = Course.objects.all()

    return render(request, 'page/course_list.html', {'courses': courses})


def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'page/add_course.html', {'form': form})



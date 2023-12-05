from .forms import CourseForm, CourseEditForm
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course, Video, User_Course
from django.shortcuts import reverse


def index(request):
    return render(request, 'page/home.html', {
        'nav': "home"
    })


def about(request):
    return render(request, 'page/about.html', {
        'nav': "about"
    })


@login_required
def course(request):
    user = request.user
    object_list = Course.objects.all()
    enrolled_courses = User_Course.objects.filter(user=user).values_list('course__id', flat=True)
    return render(request, 'page/course.html', {
        'object_list': object_list,
        'enrolled_courses': enrolled_courses,
        'user_info': user.profile if hasattr(user, 'profile') else None,
    })


def course_list(request, pk):
    course_lesson = get_object_or_404(Course, id=pk)
    video_lesson = course_lesson.videos.all()

    return render(request, 'page/course_list.html',
                  {'course': course_lesson, 'video_lesson': video_lesson})


def learn(request, pk):
    video_lesson = get_object_or_404(Video, id=pk)
    id_course = video_lesson.course.id
    list_lesson = Video.objects.filter(course=id_course)
    return render(request, 'page/learn.html', {'video_lesson': video_lesson, "list_lesson": list_lesson})


@login_required
def list_admin(request):
    object_list = Course.objects.all()
    return render(request, 'page/list_admin.html', {
        'object_list': object_list,
    })


def course_detail(request, pk):
    course_video = get_object_or_404(Course, id=pk)
    videos = course_video.videos.all()
    user_count = User_Course.objects.filter(course=course_video).count()

    return render(request, 'page/course_detail.html',
                  {'course': course_video, 'videos': videos, 'user_count': user_count})


def video_detail(request, pk):
    videos = Video.objects.filter(course_id=pk)
    return render(request, 'page/video_detail.html', {'videos': videos})


def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('course_list', pk=course.id)
    else:
        form = CourseForm()
    return render(request, 'page/add_course.html', {'form': form})


def edit_course(request, pk):
    courses = get_object_or_404(Course, id=pk)

    if request.method == 'POST':
        form = CourseEditForm(request.POST, request.FILES, instance=courses)
        if form.is_valid():
            form.save()
            return redirect('course_detail', pk=courses.id)
    else:
        form = CourseEditForm(instance=courses)

    return render(request, 'page/edit_course.html', {'form': form, 'course': courses})


def join_course(request, pk):
    course = get_object_or_404(Course, id=pk)
    user = request.user

    if not User_Course.objects.filter(course=course, user=user).exists():
        User_Course.objects.create(course=course, user=user)

    return redirect(reverse('course_list', kwargs={'pk': course.id}))

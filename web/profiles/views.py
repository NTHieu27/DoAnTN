from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from home.models import Course
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProfileEditForm


def test(request):
    return render(request, 'test.html', {})


def update_user(request):
    if request.user.is_authenticated:
        all_users = User.objects.exclude(username='admin')
        return render(request, 'update_user.html', {'profiles': all_users})
    else:
        messages.error(request, "Invalid username or password")
        return redirect('/')


@login_required(login_url='/')
def profile(request, pk):
    try:
        user = User.objects.get(id=pk)
        return render(request, 'profile.html', {'user': user})
    except User.DoesNotExist:
        messages.error(request, "Profile not found")
        return redirect('/')
    except Exception as e:
        messages.error(request, f"Đã xảy ra lỗi: {e}")
        return redirect('/')


@login_required(login_url='/')
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile', request.user.id)
        else:
            print(form.errors)
    else:
        form = ProfileEditForm(instance=request.user)

    return render(request, 'edit_profile.html', {'form': form})


def user_detail(request, pk):
    user = get_object_or_404(User, id=pk)
    # breakpoint()
    return render(request, 'user_detail.html', {'profile': user})



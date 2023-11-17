from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'educator', 'excerpt', 'description', 'num_lessons', 'picture']

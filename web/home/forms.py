from django import forms
from .models import Course, Video


class CourseForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    educator = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    excerpt = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    num_lessons = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    picture = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))

    video_title = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    video_description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    course_video = forms.FileField(required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Course
        fields = ['name', 'educator', 'excerpt', 'description', 'num_lessons', 'picture']


def save(self, commit=True):
    course = super(CourseForm, self).save(commit)
    video_title = self.cleaned_data.get('video_title')
    video_description = self.cleaned_data.get('video_description')
    course_video = self.cleaned_data.get('course_video')

    if video_title and course_video:
        Video.objects.create(title=video_title, description=video_description, course_video=course_video,
                             course=course)

    return course


class CourseEditForm(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    educator = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    excerpt = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    num_lessons = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # picture = forms.ImageField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Course
        fields = ['name', 'educator', 'excerpt', 'description', 'num_lessons', 'picture']

    def clean_picture(self):
        picture = self.cleaned_data.get('picture')
        if not picture and self.instance.pk:
            return Course.objects.get(pk=self.instance.pk).picture
        elif not picture:
            return None

        return picture

    def clean(self):
        cleaned_data = super().clean()
        # You can add additional validation or processing here if needed
        return cleaned_data

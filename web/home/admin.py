from django.contrib import admin
from .models import Course, Video


class VideoInline(admin.TabularInline):
    model = Video
    extra = 1


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'educator', 'excerpt', 'description', 'num_lessons', 'picture',)
    search_fields = ('name',)
    inlines = [VideoInline]


admin.site.register(Course, CourseAdmin)
admin.site.register(Video)

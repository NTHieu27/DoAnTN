from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255)
    educator = models.CharField(max_length=255)
    excerpt = models.TextField()
    description = models.TextField()
    num_lessons = models.IntegerField()
    picture = models.ImageField(upload_to='course_pictures/', null=True, blank=True)

    def __str__(self):
        return self.name


class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default="1")
    course_video = models.FileField(upload_to="course_video/", null=True, blank=True)
    # youtube_url = models.URLField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='videos')

    def __str__(self):
        return self.title

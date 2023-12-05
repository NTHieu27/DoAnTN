# test_script.py
import django
from django.conf import settings
from .models import Course, Video

# Cài đặt Django
django.setup()

# Tạo một khóa học mới
course = Course.objects.create(
    name='Tên khóa học',
    educator='Người giảng dạy',
    excerpt='Mô tả ngắn',
    description='Mô tả chi tiết',
    num_lessons=10
)

# Hiển thị thông tin về khóa học
print(course)

# Tạo và thêm video vào khóa học
video1 = Video.objects.create(
    title='Tiêu đề video 1',
    description='Mô tả video 1',
    course_video='path/to/video1.mp4'
)
course.videos.add(video1)

video2 = Video.objects.create(
    title='Tiêu đề video 2',
    description='Mô tả video 2',
    course_video='path/to/video2.mp4'
)
course.videos.add(video2)

# Lưu lại khóa học
course.save()

# Hiển thị thông tin về các video trong khóa học
videos_in_course = course.videos.all()
for video in videos_in_course:
    print(f"Video: {video.title}")

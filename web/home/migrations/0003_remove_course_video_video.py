# Generated by Django 4.2.6 on 2023-11-16 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_course_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='video',
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('description', models.TextField()),
                ('youtube_url', models.URLField(verbose_name='Đường dẫn YouTube')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.course')),
            ],
        ),
    ]
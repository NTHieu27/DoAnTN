# Generated by Django 4.2.7 on 2023-11-22 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_video_lesson'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='lesson',
        ),
    ]

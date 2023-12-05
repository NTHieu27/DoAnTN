# Generated by Django 4.2.7 on 2023-11-22 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_remove_course_videos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='home.course'),
        ),
    ]
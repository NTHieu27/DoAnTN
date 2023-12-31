# Generated by Django 4.2.6 on 2023-11-16 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_video_description_remove_video_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='description',
            field=models.TextField(default='1'),
        ),
        migrations.AddField(
            model_name='video',
            name='title',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='educator',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='course',
            name='excerpt',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='course',
            name='num_lessons',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='course_pictures/'),
        ),
        migrations.AlterField(
            model_name='video',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='home.course'),
        ),
        migrations.AlterField(
            model_name='video',
            name='youtube_url',
            field=models.URLField(),
        ),
    ]

# Generated by Django 4.2.7 on 2023-11-22 18:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_video_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='lesson',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]

# Generated by Django 4.2.20 on 2025-03-26 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_photo_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='thumbnail',
        ),
    ]

# Generated by Django 3.0.6 on 2020-09-19 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0027_remove_post_mediatype'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='mediatype',
            field=models.CharField(default='', max_length=3),
        ),
    ]

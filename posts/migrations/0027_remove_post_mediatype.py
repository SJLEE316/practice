# Generated by Django 3.0.6 on 2020-09-19 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0026_auto_20200918_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='mediatype',
        ),
    ]

# Generated by Django 3.0.6 on 2020-09-18 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0019_post_content_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content_type',
            field=models.CharField(max_length=50),
        ),
    ]

# Generated by Django 3.0.6 on 2020-09-15 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_auto_20200915_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('pub', 'pub'), ('booth', 'booth'), ('performance', 'performance'), ('etc', 'etc')], default='', max_length=300),
        ),
    ]
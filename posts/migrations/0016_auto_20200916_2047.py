# Generated by Django 3.0.6 on 2020-09-16 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_auto_20200916_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('pub', 'pub'), ('booth', 'booth'), ('performance', 'performance'), ('etc', 'etc')], max_length=300),
        ),
    ]
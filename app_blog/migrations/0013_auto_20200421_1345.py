# Generated by Django 3.0.5 on 2020-04-21 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0012_auto_20200421_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_title',
            field=models.CharField(max_length=200, unique=True, verbose_name='title'),
        ),
    ]

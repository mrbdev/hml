# Generated by Django 3.0.5 on 2020-04-21 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0008_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_tags',
            field=models.ManyToManyField(to='app_blog.Tag'),
        ),
    ]

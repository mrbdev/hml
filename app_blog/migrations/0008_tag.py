# Generated by Django 3.0.5 on 2020-04-20 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0007_auto_20200420_2344'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag_id', models.AutoField(primary_key=True, serialize=False)),
                ('tag_name', models.CharField(max_length=25, unique=True)),
            ],
        ),
    ]

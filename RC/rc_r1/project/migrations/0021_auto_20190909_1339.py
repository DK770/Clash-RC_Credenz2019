# Generated by Django 2.2.3 on 2019-09-09 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0020_profile_visited'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='attempted',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='correct',
            field=models.IntegerField(default=0),
        ),
    ]

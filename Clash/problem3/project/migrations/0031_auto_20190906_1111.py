# Generated by Django 2.0.1 on 2019-09-06 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0030_auto_20190905_2134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='remain_time',
        ),
        migrations.AddField(
            model_name='profile',
            name='stack',
            field=models.IntegerField(default=0),
        ),
    ]

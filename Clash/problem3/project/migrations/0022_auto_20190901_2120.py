# Generated by Django 2.2.3 on 2019-09-01 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0021_profile_visited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='visited',
            field=models.CharField(default='', max_length=100),
        ),
    ]

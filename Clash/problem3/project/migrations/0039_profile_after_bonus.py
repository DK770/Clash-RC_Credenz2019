# Generated by Django 2.2.3 on 2019-09-10 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0038_profile_curqno'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='after_bonus',
            field=models.IntegerField(default=0),
        ),
    ]

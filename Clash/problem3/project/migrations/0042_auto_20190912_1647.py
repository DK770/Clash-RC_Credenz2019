# Generated by Django 2.2.3 on 2019-09-12 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0041_auto_20190910_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='attempted',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='curqno',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='profile',
            name='endian_counter',
            field=models.IntegerField(default=0),
        ),
    ]

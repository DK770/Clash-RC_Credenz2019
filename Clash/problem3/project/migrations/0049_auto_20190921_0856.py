# Generated by Django 2.2.3 on 2019-09-21 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0048_auto_20190920_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]

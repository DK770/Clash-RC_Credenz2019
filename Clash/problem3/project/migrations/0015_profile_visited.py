# Generated by Django 2.2.3 on 2019-08-28 10:41

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0014_auto_20190827_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='visited',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), default=0, size=None),
            preserve_default=False,
        ),
    ]

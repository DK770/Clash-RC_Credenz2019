# Generated by Django 2.0.1 on 2019-09-17 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0024_profile_att1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='att1',
            field=models.CharField(default='', max_length=100),
        ),
    ]

# Generated by Django 2.0.1 on 2019-09-01 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0015_auto_20190831_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='username',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='response',
            name='attempt1',
            field=models.IntegerField(default=-32768),
        ),
        migrations.AlterField(
            model_name='response',
            name='attempt2',
            field=models.IntegerField(default=32768),
        ),
    ]

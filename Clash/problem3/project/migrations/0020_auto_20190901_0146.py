# Generated by Django 2.2.3 on 2019-08-31 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0019_remove_profile_visited'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='year',
        ),
        migrations.AddField(
            model_name='profile',
            name='level',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='profile',
            name='buff_cntr',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='questions',
            name='level',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='response',
            name='resp',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]
# Generated by Django 2.0.1 on 2019-08-29 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_auto_20190829_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mob1',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mob2',
            field=models.CharField(default='9999999999', max_length=10),
        ),
    ]

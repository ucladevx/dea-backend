# Generated by Django 2.0.5 on 2018-05-23 06:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0003_auto_20180523_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchedusers',
            name='meal_datetime',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='meal_datetime'),
        ),
    ]
# Generated by Django 2.0.5 on 2019-02-09 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0009_auto_20180603_0301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='waitinguser',
            name='found_match',
        ),
        migrations.AddField(
            model_name='waitinguser',
            name='status',
            field=models.CharField(choices=[('C', 'CANCELLED'), ('S', 'SUCCESS'), ('P', 'PENDING'), ('T', 'TIMEOUT')], default='P', max_length=1, verbose_name='status'),
        ),
    ]

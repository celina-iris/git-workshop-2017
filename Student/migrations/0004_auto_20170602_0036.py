# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0003_auto_20170602_0034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='student',
        ),
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.ManyToManyField(to='Student.Course'),
        ),
    ]

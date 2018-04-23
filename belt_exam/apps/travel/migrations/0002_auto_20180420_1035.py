# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-20 17:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='travel_plan',
        ),
        migrations.AddField(
            model_name='user',
            name='travel_plans',
            field=models.ManyToManyField(related_name='users_plans', to='travel.Travel'),
        ),
    ]

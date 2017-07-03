# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 11:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_userprofile_follows'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='subscription_end',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

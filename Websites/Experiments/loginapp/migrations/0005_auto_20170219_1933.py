# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 19:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0004_auto_20170219_0739'),
    ]

    operations = [
        migrations.RenameField(
            model_name='session_log',
            old_name='session_acton',
            new_name='session_action',
        ),
        migrations.AddField(
            model_name='questions',
            name='session',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='loginapp.Session_log'),
            preserve_default=False,
        ),
    ]

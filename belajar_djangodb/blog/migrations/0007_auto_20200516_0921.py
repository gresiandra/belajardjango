# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-16 02:21
from __future__ import unicode_literals

import blog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200512_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, validators=[blog.validators.validate_title]),
        ),
    ]

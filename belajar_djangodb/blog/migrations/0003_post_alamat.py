# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-06 02:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='alamat',
            field=models.TextField(blank=True),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-10 07:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='alamat',
            field=models.TextField(),
        ),
    ]

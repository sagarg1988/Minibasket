# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-02 09:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0002_item_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_deleted',
            field=models.BooleanField(default=True),
        ),
    ]

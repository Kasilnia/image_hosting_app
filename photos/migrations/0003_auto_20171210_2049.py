# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-10 20:49
from __future__ import unicode_literals

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20171210_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '600x600', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='Photo cropping'),
        ),
    ]

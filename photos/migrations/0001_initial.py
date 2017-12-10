# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-10 01:04
from __future__ import unicode_literals

from django.db import migrations, models
import image_cropping.fields
import stdimage.models
import stdimage.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('image', stdimage.models.StdImageField(upload_to=stdimage.utils.UploadToClassNameDir(), verbose_name='Image')),
                ('cropping', image_cropping.fields.ImageRatioField('image', '100x100', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='Photo cropping')),
            ],
            options={
                'verbose_name_plural': 'Photos',
                'verbose_name': 'Photo',
            },
        ),
    ]
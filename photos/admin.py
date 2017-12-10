# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from image_cropping import ImageCroppingMixin

from .models import Photo


@admin.register(Photo)
class PhotoAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

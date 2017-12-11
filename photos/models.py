# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from image_cropping import ImageRatioField


class Photo(models.Model):
    """Photo model stores image file."""
    title = models.CharField(_('Title'), max_length=150)
    image = models.ImageField(_('Image'), upload_to='photos')
    cropping = ImageRatioField(
        'image', '600x600', size_warning=True,
        verbose_name=_('Photo cropping'))
    slug = models.SlugField(
        _('Slug'),
        help_text=_('it\'s a string, which is shown in url address'),
        blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Photo')
        verbose_name_plural = _('Photos')
        ordering = ('title',)  # TODO Add sorting after datetime

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Photo, self).save(*args, **kwargs)

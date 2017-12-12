# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from jsonfield import JSONField

from image_cropping import ImageRatioField

from .utils import get_visual_report


class Photo(models.Model):
    """Photo model stores image file."""

    title = models.CharField(_('Title'), max_length=150)
    image = models.ImageField(_('Image'), upload_to='photos')
    cropping = ImageRatioField(
        'image', '600x600', size_warning=True,
        verbose_name=_('Photo cropping'))
    visual_report = JSONField(blank=True, null=True)
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

    def get_absolute_url(self):
        return reverse_lazy('photos:detail_photo',
                            kwargs={'pk': self.pk, 'slug': self.slug})

    def report_labels(self):
        try:
            return self.visual_report['responses'][0]['labelAnnotations']
        except:
            return None


@receiver(post_save, sender=Photo)
def vision_analysis(sender, **kwargs):
    """Connect with google vision api and receives visual report."""
    instance = kwargs['instance']
    instance_query = Photo.objects.filter(pk=instance.pk)
    try:
        visual_report = get_visual_report(instance.image)
        instance_query.update(visual_report=visual_report)
    except:
        pass

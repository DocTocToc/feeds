#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-
# vim: ts=4 et sw=4 sts=4

"""
Feed-Aggregator models.
=======================

Stores as much as possible coming out of the feed.

.. moduleauthor:: Andreas Neumeier <andreas@neumeier.org>
"""

import logging

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify

from ..managers import SiteManager

logger = logging.getLogger(__name__)


class Site(models.Model):
    url = models.URLField(unique=True)
    """URL of the `Site`."""

    slug = models.SlugField(null=True)
    """Human readble URL component"""

    objects = SiteManager()
    """
    Overwrite the inherited manager
    with the custom :mod:`feeds.models.SiteManager`
    """

    def save(self, *args, **kwargs):
        """
        Since 'slug' is not a required field for userinput,
        set it before saving.
        """
        if not self.slug:
            self.slug = slugify(self.url)
        return super(Site, self).save(*args, **kwargs)

    def __str__(self):
        """
        String representation of :Site:
        """
        return u"%s" % (self.url)

    @models.permalink
    def get_absolute_url(self):
        """
        Absolute URL for this object.

        ToDo: should use 'slug' instead of 'id'
        """
        return ('planet:site-view', [str(self.id)])

    def feeds(self):
        """
        return all feeds for this :Site:.
        """
        return self.feed_set.all()

    def natural_key(self):
        return (self.slug,)

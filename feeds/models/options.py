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
from django.conf import settings

from ..managers import OptionsManager
from .feed import Feed

logger = logging.getLogger(__name__)


class Options(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    number_initially_displayed = models.IntegerField(default=10)
    number_additionally_displayed = models.IntegerField(default=5)
    max_entries_saved = models.IntegerField(default=100)

    objects = OptionsManager()

    subscriptions = models.ManyToManyField(Feed, through='Subscription')

    class Meta:
        verbose_name_plural = "options"

    def __unicode__(self):
        return u'Options'
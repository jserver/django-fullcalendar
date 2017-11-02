# -*- coding: utf-8 -*-
from django.db import models

class EventYear(models.Model):
    value = models.CharField(max_length=4, unique=True)

    class Meta:
        ordering = ('value',)

    def __unicode__(self):
        return self.value

class CalendarEvent(models.Model):
    title = models.CharField(max_length=255)
    start = models.DateTimeField()
    end = models.DateTimeField()
    all_day = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    description = models.TextField(null=True, blank=True)
    years = models.ManyToManyField(EventYear, blank=True)

    class Meta:
        ordering = ('start',)
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __unicode__(self):
        return self.title

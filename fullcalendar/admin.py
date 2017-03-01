from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea

from attachments.admin import AttachmentInlines

from .models import CalendarEvent, EventISO, EventRFPType, EventState, EventUtility, EventYear


@admin.register(EventISO)
class EventISOAdmin(admin.ModelAdmin):
    pass


@admin.register(EventRFPType)
class EventRFPTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(EventState)
class EventStateAdmin(admin.ModelAdmin):
    pass


@admin.register(EventUtility)
class EventUtilityAdmin(admin.ModelAdmin):
    pass


@admin.register(EventYear)
class EventYearAdmin(admin.ModelAdmin):
    pass


@admin.register(CalendarEvent)
class CalendarEventAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '200'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 100})},
    }
    date_hierarchy = 'start'
    filter_horizontal = ('utilities', 'years', 'rfp_types')
    inlines = (AttachmentInlines,)
    list_display = ('title', 'start', 'end', 'iso', 'state', 'active')
    list_filter = ('iso', 'state')

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fullcalendar', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calendarevent',
            name='iso',
        ),
        migrations.RemoveField(
            model_name='calendarevent',
            name='rfp_types',
        ),
        migrations.RemoveField(
            model_name='calendarevent',
            name='state',
        ),
        migrations.RemoveField(
            model_name='calendarevent',
            name='utilities',
        ),
        migrations.DeleteModel(
            name='EventISO',
        ),
        migrations.DeleteModel(
            name='EventRFPType',
        ),
        migrations.DeleteModel(
            name='EventState',
        ),
        migrations.DeleteModel(
            name='EventUtility',
        ),
    ]

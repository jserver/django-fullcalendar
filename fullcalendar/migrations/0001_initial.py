# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('all_day', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'ordering': ('start',),
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='EventISO',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=10)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='EventRFPType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(unique=True, max_length=50)),
            ],
            options={
                'ordering': ('value',),
            },
        ),
        migrations.CreateModel(
            name='EventState',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('abbrev', models.CharField(unique=True, max_length=2)),
                ('name', models.CharField(unique=True, max_length=20)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='EventUtility',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='EventYear',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(unique=True, max_length=4)),
            ],
            options={
                'ordering': ('value',),
            },
        ),
        migrations.AddField(
            model_name='calendarevent',
            name='iso',
            field=models.ForeignKey(blank=True, to='fullcalendar.EventISO', null=True),
        ),
        migrations.AddField(
            model_name='calendarevent',
            name='rfp_types',
            field=models.ManyToManyField(to='fullcalendar.EventRFPType', verbose_name=b'RFP Types', blank=True),
        ),
        migrations.AddField(
            model_name='calendarevent',
            name='state',
            field=models.ForeignKey(blank=True, to='fullcalendar.EventState', null=True),
        ),
        migrations.AddField(
            model_name='calendarevent',
            name='utilities',
            field=models.ManyToManyField(to='fullcalendar.EventUtility', blank=True),
        ),
        migrations.AddField(
            model_name='calendarevent',
            name='years',
            field=models.ManyToManyField(to='fullcalendar.EventYear', blank=True),
        ),
    ]

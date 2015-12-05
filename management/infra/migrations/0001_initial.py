# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoreKeyMouse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keyboard_brand', models.CharField(max_length=20)),
                ('keyboard_count', models.IntegerField(default=1)),
                ('mouse_brand', models.CharField(max_length=20)),
                ('mouse_count', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='CoreMisc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('misc_item', models.CharField(max_length=25)),
                ('misc_item_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CoreMonitors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('monitor_brand', models.CharField(max_length=20)),
                ('monitor_size', models.IntegerField()),
                ('monitor_type', models.CharField(max_length=10)),
                ('monitor_count', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='CoreOS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('os_flavor', models.CharField(max_length=15)),
                ('os_arch', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CoreProcessors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('processor_brand', models.CharField(max_length=20)),
                ('processor_freq', models.FloatField()),
                ('processor_type', models.CharField(max_length=20)),
                ('processor_arch', models.IntegerField()),
                ('processor_count', models.IntegerField(default=1)),
            ],
        ),
    ]

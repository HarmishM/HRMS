# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infra', '0002_auto_20151125_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='coremonitors',
            name='monitor_brand_cnt',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='coremonitors',
            name='monitor_size_cnt',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='coremonitors',
            name='monitor_type_cnt',
            field=models.IntegerField(default=0),
        ),
    ]

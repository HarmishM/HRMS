# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infra', '0004_remove_coremonitors_monitor_brand_cnt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coremonitors',
            name='monitor_size_cnt',
        ),
    ]

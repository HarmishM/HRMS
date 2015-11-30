# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infra', '0003_auto_20151126_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coremonitors',
            name='monitor_brand_cnt',
        ),
    ]

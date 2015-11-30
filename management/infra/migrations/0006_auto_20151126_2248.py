# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infra', '0005_remove_coremonitors_monitor_size_cnt'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coremonitors',
            old_name='monitor_type_cnt',
            new_name='monitor_count',
        ),
    ]

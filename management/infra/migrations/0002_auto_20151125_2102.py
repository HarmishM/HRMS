# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infra', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coreos',
            name='os_flavor',
            field=models.CharField(max_length=15),
        ),
    ]

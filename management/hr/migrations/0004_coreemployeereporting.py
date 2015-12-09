# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0003_auto_20151208_2245'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoreEmployeeReporting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reporting_type', models.CharField(max_length=20, null=True, blank=True)),
                ('employee_id', models.ForeignKey(related_name='employee_reporting_for', to='hr.CoreEmployee')),
                ('supervisor_id', models.ForeignKey(related_name='employee_reporting_to', to='hr.CoreEmployee')),
            ],
        ),
    ]

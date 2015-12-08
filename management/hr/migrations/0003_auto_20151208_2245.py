# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0002_auto_20151208_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coreemployeecontact',
            name='employee',
            field=models.ForeignKey(related_name='employees_contact', to='hr.CoreEmployee'),
        ),
    ]

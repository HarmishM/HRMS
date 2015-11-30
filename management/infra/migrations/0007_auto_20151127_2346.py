# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infra', '0006_auto_20151126_2248'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoreMisc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('misc_item', models.CharField(max_length=25)),
                ('misc_item_count', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='corekeymouse',
            name='keyboard_count',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='corekeymouse',
            name='mouse_count',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='coreprocessors',
            name='processor_count',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='coremonitors',
            name='monitor_count',
            field=models.IntegerField(default=1),
        ),
    ]

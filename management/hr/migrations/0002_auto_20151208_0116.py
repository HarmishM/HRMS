# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoreEmployeeJob',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('empl_department', models.CharField(max_length=40, null=True, blank=True)),
                ('empl_designation', models.CharField(max_length=40, null=True, blank=True)),
                ('empl_job_type', models.CharField(max_length=40, null=True, blank=True)),
                ('empl_join_date', models.DateField(null=True, blank=True)),
                ('empl_job_location', models.CharField(max_length=50, null=True, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='coreemployee',
            name='empl_department',
        ),
        migrations.RemoveField(
            model_name='coreemployee',
            name='empl_designation',
        ),
        migrations.RemoveField(
            model_name='coreemployee',
            name='empl_join_date',
        ),
        migrations.RemoveField(
            model_name='coreemployee',
            name='empl_pre_org',
        ),
        migrations.RemoveField(
            model_name='coreemployee',
            name='empl_project',
        ),
        migrations.AddField(
            model_name='coreemployeejob',
            name='employee',
            field=models.ForeignKey(to='hr.CoreEmployee'),
        ),
    ]

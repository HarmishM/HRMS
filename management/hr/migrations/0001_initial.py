# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoreDeparDesig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('department', models.CharField(max_length=40)),
                ('designation', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='CoreEmployee',
            fields=[
                ('empl_id', models.AutoField(serialize=False, primary_key=True)),
                ('empl_fname', models.CharField(max_length=30)),
                ('empl_mname', models.CharField(max_length=30)),
                ('empl_lname', models.CharField(max_length=30)),
                ('empl_dob', models.DateField(default=datetime.date.today)),
                ('empl_department', models.CharField(max_length=40)),
                ('empl_designation', models.CharField(max_length=40)),
                ('empl_project', models.CharField(max_length=40)),
                ('empl_join_date', models.DateField(default=datetime.date.today)),
                ('empl_pre_org', models.CharField(default=b'Fresher', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectManager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project', models.CharField(max_length=40)),
                ('manager', models.ForeignKey(to='hr.CoreEmployee')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


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
                ('empl_dob', models.DateField(default=None, null=True, blank=True)),
                ('empl_department', models.CharField(max_length=40)),
                ('empl_designation', models.CharField(max_length=40)),
                ('empl_project', models.CharField(max_length=40)),
                ('empl_join_date', models.DateField(default=None, null=True, blank=True)),
                ('empl_pre_org', models.CharField(max_length=50)),
                ('empl_pic', models.FileField(default=None, upload_to=b'employee_pics/')),
                ('empl_driving_licence_number', models.CharField(max_length=30)),
                ('driving_licence_expiry', models.DateField(null=True)),
                ('empl_marital_status', models.CharField(max_length=12, null=True)),
                ('empl_gender', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CoreEmployeeContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('addr_line1', models.CharField(max_length=60, null=True, blank=True)),
                ('addr_line2', models.CharField(max_length=60, null=True, blank=True)),
                ('city', models.CharField(max_length=30, null=True, blank=True)),
                ('state', models.CharField(max_length=30, null=True, blank=True)),
                ('country', models.CharField(max_length=30, null=True, blank=True)),
                ('zip_code', models.CharField(max_length=12, null=True, blank=True)),
                ('home_phone', models.CharField(max_length=15, null=True, blank=True)),
                ('mobile', models.CharField(max_length=15, null=True, blank=True)),
                ('personal_email', models.EmailField(max_length=70, null=True, blank=True)),
                ('employee', models.ForeignKey(to='hr.CoreEmployee')),
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

from django.db import models
import datetime


class CoreEmployee(models.Model):
    empl_id = models.AutoField(primary_key=True)
    empl_fname = models.CharField(max_length=30)
    empl_mname = models.CharField(max_length=30)
    empl_lname = models.CharField(max_length=30)
    empl_dob = models.DateField(null=True, default=None, blank=True)
    empl_department = models.CharField(max_length=40)
    empl_designation = models.CharField(max_length=40)
    empl_project = models.CharField(max_length=40)
    empl_join_date = models.DateField(default=None, null=True, blank=True)
    empl_pre_org = models.CharField(max_length=50)
    empl_pic = models.FileField(upload_to='employee_pics/', default=None)
    empl_driving_licence_number = models.CharField(max_length=30)
    driving_licence_expiry = models.DateField(null=True)
    empl_marital_status = models.CharField(max_length=12)
    empl_gender = models.CharField(max_length=10)


class CoreDeparDesig(models.Model):
    department = models.CharField(max_length=40)
    designation = models.CharField(max_length=40)


class ProjectManager(models.Model):
    project = models.CharField(max_length=40)
    manager = models.ForeignKey(CoreEmployee)

from django.db import models
import datetime

class CoreEmployee(models.Model):
	empl_id = models.AutoField(primary_key=True)
	empl_fname = models.CharField(max_length=30)
	empl_mname = models.CharField(max_length=30)
	empl_lname = models.CharField(max_length=30)
	empl_dob = models.DateField(default=datetime.date.today)
	empl_department = models.CharField(max_length=40)
	empl_designation = models.CharField(max_length=40)
	empl_project = models.CharField(max_length=40)
	empl_join_date = models.DateField(default=datetime.date.today)
	empl_pre_org = models.CharField(max_length=50, default='Fresher')

class CoreDeparDesig(models.Model):
	department = models.CharField(max_length=40)
	designation = models.CharField(max_length=40)

class ProjectManager(models.Model):
	project = models.CharField(max_length=40)
	manager = models.ForeignKey(CoreEmployee)

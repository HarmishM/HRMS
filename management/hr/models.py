from django.db import models

''' Employees's primary details table '''


class CoreEmployee(models.Model):
    empl_id = models.AutoField(primary_key=True)
    empl_fname = models.CharField(max_length=30)
    empl_mname = models.CharField(max_length=30)
    empl_lname = models.CharField(max_length=30)
    empl_dob = models.DateField(null=True, default=None, blank=True)
    empl_pic = models.FileField(upload_to='employee_pics/', default=None)
    empl_driving_licence_number = models.CharField(max_length=30)
    driving_licence_expiry = models.DateField(null=True)
    empl_marital_status = models.CharField(max_length=12, null=True)
    empl_gender = models.CharField(max_length=10, null=True)


''' Employee's contact info. 'll be stored in the below table,
    ``empl_id`` of ``CoreEmployee`` will serve as PK for this. '''


class CoreEmployeeContact(models.Model):
    employee = models.ForeignKey(CoreEmployee,related_name='employees_contact')
    addr_line1 = models.CharField(max_length=60, null=True, blank=True)
    addr_line2 = models.CharField(max_length=60, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    state = models.CharField(max_length=30, null=True, blank=True)
    country = models.CharField(max_length=30, null=True, blank=True)
    zip_code = models.CharField(max_length=12, null=True, blank=True)
    home_phone = models.CharField(max_length=15, null=True, blank=True)
    mobile = models.CharField(max_length=15, null=True, blank=True)
    personal_email = models.EmailField(max_length=70, null=True, blank=True)


''' Employee's Job info. 'll be stored in the below table,
    ``empl_id`` of ``CoreEmployee`` will serve as PK for this. '''


class CoreEmployeeJob(models.Model):
    employee = models.ForeignKey(CoreEmployee)
    empl_department = models.CharField(max_length=40, null=True, blank=True)
    empl_designation = models.CharField(max_length=40, null=True, blank=True)
    empl_job_type = models.CharField(max_length=40, null=True, blank=True)
    empl_join_date = models.DateField(null=True, blank=True)
    empl_job_location = models.CharField(max_length=50, null=True, blank=True)


''' Employee's Reporting info. 'll be stored in the below table,
    ``empl_id`` of ``CoreEmployee`` will serve as PK for this,
     also ``supervisor_id`` will also be FK to ``CoreEmployee``.'''


class CoreEmployeeReporting(models.Model):
    employee_id = models.ForeignKey(CoreEmployee, related_name='employee_reporting_for')
    supervisor_id = models.ForeignKey(CoreEmployee, related_name='employee_reporting_to')
    reporting_type = models.CharField(max_length=20, null=True, blank=True)


class CoreDeparDesig(models.Model):
    department = models.CharField(max_length=40)
    designation = models.CharField(max_length=40)


class ProjectManager(models.Model):
    project = models.CharField(max_length=40)
    manager = models.ForeignKey(CoreEmployee)

from django.conf.urls import include, url
from django.contrib import admin
from hr.views import *


urlpatterns = [
    url(r'^api/ajax/departments/$', deliever_dep_desig, name='Get-Departments'),
    url(r'^api/ajax/reporting/update/$', update_reporting_details, name='Update-reporting-info'),
    url(r'^api/ajax/reporting/delete/$', delete_supervisor, name='Delete-reporting-info'),
    url(r'^api/ajax/personal/update/', update_personal_details, name='Update-personal-info'),
    url(r'^api/ajax/contacts/update/', update_contact_details, name='Update-contact-info'),
    url(r'^api/ajax/job/update/', update_job_details, name='Update-Job-info'),
    url(r'^new-employee-details/$', feed_new_empl_details, name='Primary-info-new-employee'),
    url(r'^full-employee-info/(?P<emp_id>[0-9]*)/$', full_employee_info, name='Full-employee-info'),

    url(r'^list-employees/$', list_employees, name='Employee-List'),
]
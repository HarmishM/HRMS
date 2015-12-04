from django.conf.urls import include, url
from django.contrib import admin
from hr.views import *

urlpatterns = {
    url(r'^api/ajax/departments/$', deliever_dep_desig),
    url(r'^api/ajax/personal/update', update_personal_details, name='Update-personal-info'),
    url(r'^new-employee-details/$', feed_new_empl_details, name='Primary-info-new-employee'),
    url(r'^full-employee-info/(?P<emp_id>[0-9]*)/$', full_employee_info, name='Full-employee-info'),
}
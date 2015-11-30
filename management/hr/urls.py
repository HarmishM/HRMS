from django.conf.urls import include, url
from django.contrib import admin
from hr.views import *

urlpatterns = [
	url(r'^api/ajax/departments/$', deliever_dep_desig),
	url(r'^new-employee-details/$', feed_new_empl_details),
]
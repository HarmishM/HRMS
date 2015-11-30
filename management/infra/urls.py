from django.conf.urls import include, url
from django.contrib import admin
from infra.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'management.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^assign-hardwares/$', feed_infra_details),
    url(r'^monitors/$', get_monitors, name="Get-AJax-Monitors"),
    url(r'^monitors-count/$', get_monitors_count, name="Get-AJax-Monitors-Count"),
]
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    # Examples:
    # url(r'^$', 'management.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hr/', include('hr.urls')),
    url(r'^infra/', include('infra.urls')),
]
urlpatterns += staticfiles_urlpatterns()
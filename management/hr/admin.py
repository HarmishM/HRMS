from django.contrib import admin
from hr.models import *
from django.contrib.admin import *

class CoreEmployeeAdmin(admin.ModelAdmin):
    pass


class CoreDeparDesigAdmin(admin.ModelAdmin):
    list_display = ['department', 'designation']
    search_fields = ['department']
    list_filter = ('department', 'designation')


class CoreEmployeeContactAdmin(admin.ModelAdmin):
    list_display = ['employee_id', 'addr_line1']

admin.site.register(CoreDeparDesig, CoreDeparDesigAdmin)
admin.site.register(CoreEmployee)
admin.site.register(CoreEmployeeContact, CoreEmployeeContactAdmin)
admin.site.register(CoreEmployeeJob)
admin.site.register(CoreEmployeeReporting)

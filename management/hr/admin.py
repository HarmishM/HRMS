from django.contrib import admin
from hr.models import *
from django.contrib.admin import *

class CoreEmployeeAdmin(admin.ModelAdmin):
	pass


class CoreDeparDesigAdmin(admin.ModelAdmin):
	list_display = ['department', 'designation']
	search_fields = ['department']
	list_filter = ('department', 'designation')

admin.site.register(CoreDeparDesig, CoreDeparDesigAdmin)
admin.site.register(CoreEmployee)
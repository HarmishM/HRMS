from django.contrib.admin import *
from django.contrib import admin
from infra.models import *
from django.db import models

class CoreProcessorAdmin(admin.ModelAdmin):
	fields = ('processor_brand', 'processor_freq', \
		'processor_type', 'processor_arch')
	list_display = ['processor_brand', 'processor_freq', \
		'processor_type', 'processor_arch']
	search_fields = ['processor_type']

class CoreMonitorAdmin(admin.ModelAdmin):
	'''
	fields = ('monitor_brand', 'monitor_size', \
		'monitor_type')
	'''
	list_display = ['monitor_brand', 'monitor_size', \
		 'monitor_type', 'monitor_count']
	search_fields = ['monitor_size', 'monitor_type']
	list_filter = ('monitor_size', 'monitor_type')

class CoreOSAdmin(admin.ModelAdmin):
	list_display = ['os_flavor', 'os_arch']
	list_filter = ('os_flavor', 'os_arch')

class CoreKeyMouseAdmin(admin.ModelAdmin):
	list_display = ['keyboard_brand', 'keyboard_count', \
	'mouse_brand', 'mouse_count']

class CoreMiscAdmin(admin.ModelAdmin):
	list_display = ['misc_item', 'misc_item_count']

admin.site.register(CoreMonitors, CoreMonitorAdmin)
admin.site.register(CoreProcessors, CoreProcessorAdmin)
admin.site.register(CoreKeyMouse, CoreKeyMouseAdmin)
admin.site.register(CoreOS, CoreOSAdmin)
admin.site.register(CoreMisc, CoreMiscAdmin)

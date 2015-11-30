from django.db import models

__all__ = ['CoreMonitors', 'CoreProcessors',\
		'CoreKeyMouse', 'CoreOS', 'CoreMisc']

class CoreMonitors(models.Model):
	monitor_brand = models.CharField(max_length=20)
	monitor_size = models.IntegerField()
	monitor_type = models.CharField(max_length=10)
	monitor_count = models.IntegerField(default=1)

class CoreProcessors(models.Model):
	processor_brand = models.CharField(max_length=20)
	processor_freq = models.FloatField()
	processor_type = models.CharField(max_length=20)
	processor_arch = models.IntegerField()
	processor_count = models.IntegerField(default=1)

class CoreKeyMouse(models.Model):
	keyboard_brand = models.CharField(max_length=20)
	keyboard_count = models.IntegerField(default=1)
	mouse_brand = models.CharField(max_length=20)
	mouse_count = models.IntegerField(default=1)

class CoreOS(models.Model):
	os_flavor = models.CharField(max_length=15)
	os_arch = models.IntegerField()

class CoreMisc(models.Model):
	misc_item = models.CharField(max_length=25)
	misc_item_count = models.IntegerField()

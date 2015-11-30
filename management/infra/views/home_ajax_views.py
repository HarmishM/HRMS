from infra.models import *
from django.http import HttpResponse
import json
from django.views.decorators.csrf import *

# APIs that would be called by Ajax requests during page loading
def get_monitors(request):
	if request.method == 'GET':
		monitor_brand_list, monitor_size_list, monitor_type_list = [], [], []
		monitors_dct = {}
		monitor_objs = CoreMonitors.objects.all()
		for obj in monitor_objs:
			if obj.monitor_brand not in monitor_brand_list:
				monitor_brand_list.append(obj.monitor_brand)
			if obj.monitor_size not in monitor_size_list:
				monitor_size_list.append(obj.monitor_size)
			if obj.monitor_type not in monitor_type_list:
				monitor_type_list.append(obj.monitor_type)

		monitors_dct['monitor_brand'] = monitor_brand_list
		monitors_dct['monitor_size'] = monitor_size_list
		monitors_dct['monitor_type'] = monitor_type_list

		monitors_json = json.dumps(monitors_dct)
		return HttpResponse(monitors_json, content_type='application/json')

@csrf_exempt
def get_monitors_count(request):
	if request.method == 'POST':
		#print 'yep in'
		mon_brand = request.POST.get('mon_brand')
		mon_size = request.POST.get('mon_size')
		mon_type = request.POST.get('mon_type')
		#print mon_brand, mon_size, mon_type
		count = CoreMonitors.objects.filter(monitor_brand=mon_brand,\
			monitor_size=mon_size, monitor_type=mon_type)
		if count:
			if len(count) > 1:
				final_count = 0
				for c in count:
					final_count += c.monitor_count
			else:
				final_count = count[0].monitor_count
			return HttpResponse(json.dumps(final_count))
		return HttpResponse(json.dumps(0))

def get_processors(request):
	if request.method == 'GET':
		processor_brand_list, processor_freq_list, \
		processor_type_list, processor_arch_list = [], [], [], []
		processors_dct = {}
		processors_obj = CoreProcessors.objects.all()
		for obj in processors_obj:
			processor_brand_list.append(obj.processor_brand)
			processor_freq_list.append(obj.processor_freq)
			processor_type_list.append(obj.processor_type)
			processor_arch_list.append(obj.processor_arch)
		processors_dct['processor_brand'] = processor_brand_list
		processors_dct['processor_freq'] = processor_freq_list
		processors_dct['processor_type'] = processor_type_list
		processors_dct['processor_arch'] = processor_arch_list

		processors_json = json.dumps(processors_dct)
		return HttpResponse(processors_json, content_type='application/json')



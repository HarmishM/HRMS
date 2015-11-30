from django.shortcuts import render
from django.views.decorators.csrf import *

@csrf_protect
def feed_new_empl_details(request):
	if request.method == 'GET':
		return render(request, 'new-employee/feed_employee.html')
	elif request.method == 'POST':
		print 'In Here POST'

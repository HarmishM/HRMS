from django.shortcuts import render, redirect
from django.views.decorators.csrf import *
from hr.models import *
from django.contrib import messages
from django.core.urlresolvers import reverse
from datetime import datetime

@csrf_protect
def feed_new_empl_details(request):
	if request.method == 'GET':
		try:
			curr_pk_obj = CoreEmployee.objects.order_by('-empl_id')[0]
			curr_pk = curr_pk_obj.empl_id + 1
		except IndexError:
			curr_pk = 1
		#print curr_pk
		contxt = {'emp_pk': '#'+str(curr_pk)}
		return render(request, 'new-employee/feed_employee.html', contxt)
	elif request.method == 'POST':
		print 'In Here POST'
		new_emp_id = (request.POST.get('employee_code')).split('#')[1]
		new_emp_firstname = request.POST.get('firstname')
		new_emp_middlename = request.POST.get('middlename')
		new_emp_lastname = request.POST.get('lastname')
		new_emp_dob = request.POST.get('dob')
		print new_emp_id, new_emp_firstname, new_emp_middlename, new_emp_lastname, new_emp_dob
		date_obj = datetime.strptime(new_emp_dob, '%m/%d/%Y')
		converted_date_obj = date_obj.strftime('%Y-%m-%d')

		''' this is worst and hard to happen case, where we check if the primary key,
		sent by the backend itself exist before saving it. This double checks the key
		integrity '''

		obj, created = CoreEmployee.objects.get_or_create(empl_id=new_emp_id)
		if not created:
			err_msg = 'There looks some problem with server, try once again please or please contact Administrator !'
			messages.add_message(request, messages.WARNING, err_msg)

			''' need to send email in this situaltion to admin, will be written later, and return
			same page '''
			return redirect(reverse('Primary-info-new-employee'))

		obj.empl_fname = new_emp_firstname
		obj.empl_mname = new_emp_middlename
		obj.empl_lname = new_emp_lastname
		obj.empl_dob = converted_date_obj
		obj.save()

		return render(request, 'new-employee/employee-details.html')

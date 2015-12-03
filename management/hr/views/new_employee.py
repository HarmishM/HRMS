from django.shortcuts import render, redirect
from django.views.decorators.csrf import *
from hr.models import *
from django.contrib import messages
from django.core.urlresolvers import reverse
from datetime import datetime
from django.http import HttpResponseNotFound, HttpResponse

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
		#print 'In Here POST'
		new_emp_id = (request.POST.get('employee_code')).split('#')[1]
		new_emp_firstname = request.POST.get('firstname')
		new_emp_middlename = request.POST.get('middlename')
		new_emp_lastname = request.POST.get('lastname')
		new_emp_dob = request.POST.get('dob')
		#print new_emp_id, new_emp_firstname, new_emp_middlename, new_emp_lastname, new_emp_dob
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

		return redirect(reverse('Full-employee-info', kwargs={'emp_id': new_emp_id}))

''' fetches the employee's personal details '''
def _get_personal_details(request_emp_id):
	personal_cntx = {}
	print request_emp_id
	try:
		emp_obj = CoreEmployee.objects.get(empl_id=request_emp_id)
	except CoreEmployee.DoesNotExist:
		print 'in exception'
		return None
	personal_cntx['fname'] = emp_obj.empl_fname
	personal_cntx['mname'] = emp_obj.empl_mname
	personal_cntx['lname'] = emp_obj.empl_lname
	personal_cntx['dob'] = emp_obj.empl_dob
	return personal_cntx

@csrf_protect
def full_employee_info(request, emp_id):
	if request.method == 'GET':
		print 'hit get full employee'
		full_employee_cntxt = {}
		'''Start getting the details of employee for received emp_id'''
		personal_cntx = _get_personal_details(emp_id)
		if personal_cntx is None:
			return HttpResponse('<h3> Employee with this ID is not found </h3>')
		full_employee_cntxt.update(personal_cntx)
		return render(request, 'new-employee/employee-details.html', full_employee_cntxt)

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from hr.models import *
from django.contrib import messages
from django.core.urlresolvers import reverse
from datetime import datetime
from django.http import HttpResponse
from utils import *


@csrf_protect
def feed_new_empl_details(request):
    if request.method == 'GET':
        try:
            curr_pk_obj = CoreEmployee.objects.order_by('-empl_id')[0]
            curr_pk = curr_pk_obj.empl_id + 1
        except IndexError:
            curr_pk = 1
        contxt = {'emp_pk': '#{0}'.format(str(curr_pk))}
        return render(request, 'new-employee/feed_employee.html', contxt)
    elif request.method == 'POST':
        new_emp_id = (request.POST.get('employee_code')).split('#')[1]
        new_emp_firstname = request.POST.get('firstname')
        new_emp_middlename = request.POST.get('middlename')
        new_emp_lastname = request.POST.get('lastname')
        new_emp_dob = request.POST.get('dob')
        date_obj = datetime.strptime(new_emp_dob, '%m/%d/%Y')
        converted_date_obj = date_obj.strftime('%Y-%m-%d')

        ''' this is worst and hard to happen case, where we check if the primary key,
        sent by the backend itself exist before saving it. This double checks the key integrity '''

        obj, created = CoreEmployee.objects.get_or_create(empl_id=new_emp_id)
        if not created:
            err_msg = 'There looks some problem with server, try once again please or please contact Administrator !'
            messages.add_message(request, messages.WARNING, err_msg)

            ''' need to send email in this situaltion to admin, will be written later, and return same page '''
            return redirect(reverse('Primary-info-new-employee'))

        obj.empl_fname = new_emp_firstname
        obj.empl_mname = new_emp_middlename
        obj.empl_lname = new_emp_lastname
        obj.empl_dob = converted_date_obj
        obj.save()

        return redirect(reverse('Full-employee-info', kwargs = {'emp_id': new_emp_id}))


''' fetches the employee's personal details '''


def _get_personal_details(emp_id):
    emp_obj = CoreEmployee.objects.get(empl_id=emp_id)
    personal_cntx = {'fname': emp_obj.empl_fname, 'mname': emp_obj.empl_mname, 'lname': emp_obj.empl_lname,
                     'dob': emp_obj.empl_dob, 'lic_number': emp_obj.empl_driving_licence_number,\
                     'lic_expiry': emp_obj.driving_licence_expiry, 'marital_status': emp_obj.empl_marital_status,
                     'gender': emp_obj.empl_gender}
    return personal_cntx

''' fetches the employee's contact details, written to handle provision of
    multiple addresses in future '''


def _get_contact_details(emp_id):
    full_contact_cntx = {}
    try:
        emp_contact_objs = CoreEmployeeContact.objects.filter(employee=CoreEmployee(empl_id=emp_id))
    except CoreEmployeeContact.DoesNotExist:
        return {}
    else:
        for obj in emp_contact_objs:
            key_prefix = list(emp_contact_objs).index(obj)
            contacts_cntx = {'{}addrs_line1'.format(key_prefix): obj.addr_line1,
                             '{}addrs_line2'.format(key_prefix): obj.addr_line2,
                             '{}addrs_city'.format(key_prefix): obj.city,
                             '{}addrs_state'.format(key_prefix): obj.state,
                             '{}addrs_country'.format(key_prefix): obj.country,
                             '{}addrs_zip'.format(key_prefix): obj.zip_code,
                             '{}home_phone'.format(key_prefix): obj.home_phone,
                             '{}mobile'.format(key_prefix): obj.mobile,
                             '{}pri_email'.format(key_prefix): obj.personal_email}
            full_contact_cntx.update(contacts_cntx)
    return full_contact_cntx


def _get_job_details(emp_id):
    try:
        emp_job_obj = CoreEmployeeJob.objects.get(employee=CoreEmployee(empl_id=emp_id))
    except CoreEmployeeJob.DoesNotExist:
        return {}
    else:
        job_cntx = {'job_dept': emp_job_obj.empl_department, 'job_desig': emp_job_obj.empl_designation,
                    'job_type': emp_job_obj.empl_job_type, 'join_date': emp_job_obj.empl_join_date,
                    'job_location': emp_job_obj.empl_job_location}
        return job_cntx


def _fetch_employee_list():
    try:
        employee_objs = CoreEmployee.objects.all().values('empl_id', 'empl_fname', 'empl_lname')
    except InternalError:
        return {}
    else:
        return employee_objs


def _get_reporting_details(emp_id):
    try:
        emp_report_objects = CoreEmployeeReporting.objects.filter(employee_id=CoreEmployee(empl_id=emp_id))
    except CoreEmployeeJob.DoesNotExist:
        return {}
    else:
        reporting_list = []
        for obj in emp_report_objects:
            dct = {'supervisor_name': '{} {}'.format(obj.supervisor_id.empl_fname, obj.supervisor_id.empl_lname),
                   'reporting_type': obj.reporting_type, 'supervisor_id': '{}{}'.format(obj.employee_id.empl_id, obj.reporting_type)}
            reporting_list.append(dct)
        return reporting_list

''' This method returns the employee's full details page with
    complete context '''


@csrf_protect
def full_employee_info(request, emp_id):
    if request.method == 'GET':
        full_employee_cntxt = {}
        try:
            emp_obj = CoreEmployee.objects.get(empl_id=emp_id)
        except CoreEmployee.DoesNotExist:
            return HttpResponse('<h3> Employee with this ID is not found </h3>')

        '''Start getting the details of employee for received emp_id'''

        personal_cntx = _get_personal_details(emp_id)
        contacts_cntx = _get_contact_details(emp_id)
        job_cntx = _get_job_details(emp_id)

        full_employee_cntxt.update(personal_cntx)
        full_employee_cntxt.update(contacts_cntx)
        full_employee_cntxt.update(job_cntx)
        list_employees = _fetch_employee_list()

        full_employee_cntxt['employees'] = list_employees
        reporting_cntx = _get_reporting_details(emp_id)
        full_employee_cntxt['reporting'] = reporting_cntx
        print full_employee_cntxt
        return render(request, 'new-employee/employee-details.html', full_employee_cntxt)


''' update personal details recieved via Ajax call '''


@csrf_exempt
def update_personal_details(request):
    if request.is_ajax() and request.method == 'POST':
        ''' Get employeeID first from the Ajax post req. If its not there then everything is vain, so
         return "Bad request" reponse, its again a double check, and not likely to happn '''

        try:
            request_employee_id = request.POST.get('empl_id')
        except KeyError as ex:
            return HttpResponse('<h3> Something bad happned </h3>')
        firstname = request.POST.get('fname')
        middlename = request.POST.get('mname')
        lastname = request.POST.get('lname')
        print firstname, middlename, lastname
        driving_licence_number = request.POST.get('drv_lcn_number')
        driving_licence_expiry = request.POST.get('lsn_expiry')
        marital_status = request.POST.get('mar_status')
        gender = request.POST.get('gender')

        ''' get the requested employee and set its properties received from request,
         double checking agin here, hard to happn '''

        try:
            obj_employee = CoreEmployee.objects.get(empl_id=request_employee_id)
        except CoreEmployee.DoesNotExist as e:
            return HttpResponse('<h3> Employee with this ID not found </h3>')
        obj_employee.empl_fname = firstname
        print firstname
        obj_employee.empl_mname = middlename
        obj_employee.empl_lname = lastname
        if driving_licence_number not in ABSURD_VALUES:
            obj_employee.empl_driving_licence_number = driving_licence_number
        if driving_licence_expiry not in ABSURD_VALUES:
            obj_employee.driving_licence_expiry = convert_date_for_backend(driving_licence_expiry)
        if marital_status not in ABSURD_VALUES:
            obj_employee.empl_marital_status = marital_status
        if gender is not None:
            obj_employee.empl_gender = gender
        else:
            obj_employee.empl_gender = None
        obj_employee.save()
        return HttpResponse('Saved Successfully')
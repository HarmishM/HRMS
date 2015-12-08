from hr.models import *
from django.views.generic import ListView
from django.shortcuts import render

'''
class EmployeeList(ListView):
    template_name = 'new-employee/list_employee.html'
    models = CoreEmployee
    context_object_name = 'emplyee_list'
    queryset = CoreEmployee.objects.prefetch_related('employees_contact').all()
    a = queryset[2].employees_contact.all()[0].mobile
    print a
'''


def list_employees(request):
    final_list = []
    employee_q_set = CoreEmployee.objects.all().order_by('empl_id')
    for employee_obj in employee_q_set:
        contxt = {}
        contxt['empl_id'] = employee_obj.empl_id
        contxt['fname'] = employee_obj.empl_fname
        contxt['lname'] = employee_obj.empl_lname
        cont_objs = CoreEmployeeContact.objects.filter(employee=employee_obj)
        contact_list = []
        for obj in cont_objs:
            contact_dct = {}
            if obj.mobile != '':
                contact_dct['mobile'] = obj.mobile
            if obj.home_phone != '':
                contact_dct['home'] = obj.home_phone
            if bool(contact_dct):
                contact_list.append(contact_dct)
        if contact_list:
            contxt['contacts'] = contact_list

        job_objs = CoreEmployeeJob.objects.filter(employee=employee_obj)
        job_list = []
        for jb in job_objs:
            job_dct = {}
            if jb.empl_department is not None:
                job_dct['dprt'] = jb.empl_department
            if jb.empl_designation is not None:
                job_dct['desg'] = jb.empl_designation
            if bool(job_dct):
                job_list.append(job_dct)
        if job_list:
            contxt['jobs'] = job_list
        final_list.append(contxt)
    return render(request, 'new-employee/list_employee.html', {'cnt': final_list})
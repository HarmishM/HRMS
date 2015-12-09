from django.http import HttpResponse
from hr.models import *
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def update_reporting_details(request):
    if request.method == 'POST':
        # print 'hit reporting module'
        empl_id = request.POST.get('empl_id')
        supervisor_id = request.POST.get('supervisor_empl_id')
        reporting_type = request.POST.get('report_type')
        print empl_id, supervisor_id, reporting_type
        ''' cehck to see first if such record already exists or not,
         althogh we are doble checking again if the employee and supervisor
         exists in database'''

        try:
            emp_obj = CoreEmployee.objects.get(empl_id=empl_id)
        except CoreEmployee.DoesNotExist:
            return HttpResponse('Employee with this ID does not exist')
        else:
            supervisor_obj = CoreEmployee.objects.get(empl_id=supervisor_id)
        obj, created = CoreEmployeeReporting.objects.get_or_create(employee_id=emp_obj,\
                                                                   supervisor_id=supervisor_obj,\
                                                                   reporting_type=reporting_type)
        if not created:
            return HttpResponse(json.dumps('This record already exists'))
        return HttpResponse('saved0')

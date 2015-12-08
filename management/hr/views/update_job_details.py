from hr.models import *
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from utils import *


@csrf_exempt
def update_job_details(request):
    if request.method == 'POST':
        ''' get post parameters first '''

        empl_id = request.POST.get('empl_id')
        empl_dept = request.POST.get('dept')
        empl_desig = request.POST.get('desg')
        empl_job_type = request.POST.get('emp_type')
        empl_join_date = request.POST.get('join_date')
        empl_job_loc = request.POST.get('job_loc')

        print empl_dept, empl_desig, empl_job_type, empl_join_date, empl_job_loc

        ''' check to see first if the requested employee is there in table i.e.
            if it has been modified befor for ``Job`` or not. If it is the get it,
            and further modify it, else create new one '''

        empl_obj, created = CoreEmployeeJob.objects.get_or_create(employee=CoreEmployee(empl_id=empl_id))
        if created:
            empl_obj.employee = CoreEmployee(empl_id=empl_id)

        ''' we don't wanna insert None, undefined any sort of stupid values,
            so check if any of the recieved values are amongst such... '''

        if empl_dept not in ABSURD_VALUES_JOB:
            if empl_dept == 'Not Selected Yet':
                empl_obj.empl_department = None
            else:
                empl_obj.empl_department = empl_dept
        if empl_desig not in ABSURD_VALUES_JOB:
            if empl_desig == 'Not Selected Yet':
                empl_obj.empl_designation = None
            else:
                empl_obj.empl_designation = empl_desig
        if empl_job_type not in ABSURD_VALUES_JOB:
            if empl_job_type == 'Not Selected Yet':
                empl_obj.empl_job_type = None
            else:
                empl_obj.empl_job_type = empl_job_type
        if empl_join_date not in ABSURD_VALUES:
            empl_obj.empl_join_date = convert_date_for_backend(empl_join_date)
        if empl_job_loc not in ABSURD_VALUES_JOB:
            if empl_job_loc == 'Not Selected Yet':
                empl_obj.empl_job_location = None
            else:
                empl_obj.empl_job_location = empl_job_loc

        ''' finally save the object with field values set above '''

        empl_obj.save()
        return HttpResponse('save success')






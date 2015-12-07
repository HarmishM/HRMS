from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from hr.models import *


@csrf_exempt
def update_contact_details(request):
    if request.method == 'POST':
        request_empl_id = request.POST.get('empl_id')
        addrs_line1 = request.POST.get('add_line1')
        empl_obj, created = CoreEmployeeContact.objects.get_or_create(employee=CoreEmployee(empl_id=request_empl_id))
        if created:
            empl_obj.employee_id = request_empl_id
        empl_obj.addr_line1 = addrs_line1

        empl_obj.save()
        return HttpResponse('saved')


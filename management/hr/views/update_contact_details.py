from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from hr.models import *


@csrf_exempt
def update_contact_details(request):
    if request.method == 'POST':
        request_empl_id = request.POST.get('empl_id')
        addrs_line1 = request.POST.get('add_line1')
        addrs_line2 = request.POST.get('add_line2')
        addrs_city = request.POST.get('city')
        addrs_state = request.POST.get('state')
        addrs_country = request.POST.get('country')
        addrs_zip = request.POST.get('zip')
        home_phone = request.POST.get('home_phone')
        mobile = request.POST.get('mobile')
        private_email = request.POST.get('pri_email')

        empl_obj, created = CoreEmployeeContact.objects.get_or_create(employee=CoreEmployee(empl_id=request_empl_id))
        if created:
            empl_obj.employee_id = request_empl_id
        empl_obj.addr_line1 = addrs_line1
        empl_obj.addr_line2 = addrs_line2
        empl_obj.city = addrs_city
        empl_obj.state = addrs_state
        empl_obj.country = addrs_country
        empl_obj.zip_code = addrs_zip
        empl_obj.home_phone = home_phone
        empl_obj.mobile = mobile
        empl_obj.personal_email = private_email

        empl_obj.save()
        return HttpResponse('saved')


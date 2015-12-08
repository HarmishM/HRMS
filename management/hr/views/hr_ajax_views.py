from django.http import HttpResponse
from django.views.decorators.csrf import *
from hr.models import *
import json


@csrf_exempt
def deliever_dep_desig(request):
    if request.method == 'GET':
        print 'yess called'
        home_dep_desig_dct = {}
        departments = CoreDeparDesig.objects.values('department').distinct()
        list_departments = [dep_obj['department'] for dep_obj in departments]
        home_dep_desig_dct['depts'] = list_departments

        '''get designations for 1st of returned departments'''

        designations_for_first = CoreDeparDesig.objects.filter(department=list_departments[0]).values('designation')
        designations_list = [desg_obj['designation'] for desg_obj in designations_for_first]
        home_dep_desig_dct['desgs'] = designations_list
        dep_desg_json = json.dumps(home_dep_desig_dct)
        return HttpResponse(dep_desg_json, content_type='application/json')

    elif request.method == 'POST':
        print 'post called'
        department = request.POST.get('department')
        print department
        if department == '':
            return HttpResponse(json.dumps(''), content_type='application/json')
        designations = CoreDeparDesig.objects.filter(department__startswith=department).values('designation')
        designations_list = [desg_obj['designation'] for desg_obj in designations]
        desigs_json = json.dumps(designations_list)
        return HttpResponse(desigs_json, content_type='application/json')

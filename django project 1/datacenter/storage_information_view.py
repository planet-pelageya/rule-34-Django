from datacenter.models import Passcard
from datacenter.models import Visit,is_visits_long
from django.shortcuts import render
from django.utils.timezone import localtime, timedelta
from datetime import datetime

def storage_information_view(request):
    non_closed_visit = Visit.objects.filter(leaved_at=None)
    visit_info = []
    for visit in non_closed_visit:
        enter = visit.entered_at
        timespend = localtime() - visit.entered_at
        visit_info.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': enter,
            "duration": timespend,
            'is_strange': is_visits_long(visit, minutes=60)
        })
    context = {
        'non_closed_visits': visit_info,  
    }
    return render(request, 'storage_information.html', context)

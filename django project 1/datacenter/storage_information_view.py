from datacenter.models import Passcard
from datacenter.models import Visit, is_visits_long
from django.shortcuts import render
from django.utils.timezone import localtime, timedelta
from datetime import datetime

def storage_information_view(request):
    non_closed_visit = Visit.objects.filter(leaved_at=None)
    person_visits = []
    for visit in non_closed_visit:
        enter_in_storage = visit.entered_at
        time_spend_in_storage = localtime() - visit.entered_at
        person_visits.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': enter_in_storage,
            'duration': time_spend_in_storage,
            'is_strange': is_visits_long(visit, minutes=60)
        })
    context = {
        'non_closed_visits': person_visits,  
    }
    return render(request, 'storage_information.html', context)

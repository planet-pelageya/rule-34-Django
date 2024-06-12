from datacenter.models import Passcard
from datacenter.models import Visit,is_visits_long, get_duration
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import localtime, timedelta



def passcard_info_view(request, passcode):
    passcard = Passcard.objects.all()[0]
    passcard = Passcard.objects.all()[0]
    person_passcard = get_object_or_404(Passcard,passcode=passcode)
    visits = Visit.objects.filter(passcard=person_passcard)
    visit_info = []
    for visit in visits:
        visit_info.append({
            'entered_at': visit.entered_at,
            'duration': get_duration(visit),
            'is_strange': is_visits_long(visit, minutes=60)
        })

    context = {'passcard': passcard, 'this_passcard_visits': visit_info}
    return render(request, 'passcard_info.html', context)


 

 

from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime, timedelta

def active_passcards_view(request):
        
    active_passcards = Passcard.objects.filter(is_active = True)
    context = {
        'active_passcards': acctive_passcards,  
    }
    return render(request, 'active_passcards.html', context)

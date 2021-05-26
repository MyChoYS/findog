from django.shortcuts import render
from findog.models import missingdog


def protectboard(request) :
    lostdoglist = missingdog.objects.all()
    context = {
        'lostdoglist': lostdoglist
    }
    return render(request, 'protect/protectboard.html', context);

def protectboard_detail(request) :
    i_dogid = request.GET['i_id']
    item = missingdog.objects.get(id=int(i_dogid))
    context = {
       'item' : item
    }
    return render(request, 'protect/protectboard_detail.html', context);
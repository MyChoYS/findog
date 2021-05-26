from django.shortcuts import render
from findog.models import missingdog


def missingboard(request) :
    lostdoglist = missingdog.objects.all()
    context = {
        'lostdoglist': lostdoglist
    }
    return render(request, 'missing/missingboard.html', context);

def missingboard_detail(request) :
    i_dogid = request.GET['i_id']
    item = missingdog.objects.get(id=int(i_dogid))
    context = {
       'item' : item
    }
    return render(request, 'missing/missingboard_detail.html', context);
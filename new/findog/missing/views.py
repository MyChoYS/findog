from django.shortcuts import render
from findog.models import *


def missingboard(request) :
    missingdoglist = missingdog.objects.all()
    context = {
        'missingdoglist': missingdoglist
    }
    return render(request, 'missing/missingboard.html', context);

def missingboard_detail(request) :
    i_dogid = request.GET['i_id']
    item = missingdog.objects.get(id=int(i_dogid))
    context = {
       'item' : item
    }
    return render(request, 'missing/missingboard_detail.html', context);
from django.shortcuts import render

# Create your views here.
from frame.db import lostdoglistDb


def base(request) :
    lostdoglist = lostdoglistDb().selectall()
    context = {
        'lostdoglist' : lostdoglist
    }

    return render(request, 'main.html', context);

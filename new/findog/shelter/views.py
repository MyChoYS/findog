from django.shortcuts import render

# Create your views here.
from findog.models import dogcenter


def dogcenters(request) :
    doglocation = dogcenter.objects.all()

    context = {
        'doglocation': doglocation
    }
    return render(request, 'dogcenter.html', context)
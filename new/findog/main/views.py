from django.shortcuts import render

# Create your views here.
from findog.models import missingdog


def main(request) :
    missingdoglist = missingdog.objects.all()
    context = {
        'missingdoglist' : missingdoglist
    }
    return render(request, 'main/main.html', context);

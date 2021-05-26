from django.shortcuts import render

# Create your views here.

def missingboard(request) :
    context = {

    }
    return render(request, 'missing/missingboard.html', context);
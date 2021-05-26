from django.shortcuts import render

# Create your views here.

def shelter(request) :
    context = {

    }
    return render(request, 'shelter/shelter.html', context);

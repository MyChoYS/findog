from django.shortcuts import render

# Create your views here.

def lostingboard(request) :
    context = {

    }
    return render(request, 'losting/lostingboard.html', context);
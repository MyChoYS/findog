from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.parsers import JSONParser

from frame.db import lostdoglistDb
from frame.login.db import MemberDb
from findog.models import dogcenter
from findog.models import missingdog
from findog.models import dogbreed
from findog.models import mydog
from findog.models import member
from findog.models import UploadModel



def base(request) :
    lostdoglist = missingdog.objects.all()
    context = {
        'lostdoglist' : lostdoglist
    }
    return render(request, 'main.html', context);



def main_board(request) :
    lostdoglist = missingdog.objects.all()
    context = {
        'lostdoglist': lostdoglist
    }
    return render(request, 'main_board.html', context);

def main_board_detail(request) :
    i_dogid = request.GET['i_id']
    item = missingdog.objects.get(id=int(i_dogid))
    context = {
       'item' : item
    }
    return render(request, 'main_board_detail.html', context);


#동물보호센터 현재위치 비교
def dogcenters(request) :
    doglocation = dogcenter.objects.all()

    context = {
        'doglocation': doglocation
    }
    return render(request, 'dogcenter.html', context)

#파일업로드
def exam2(request) :
    context = None
    if request.method == 'POST' :
        upload = UploadModel(title = request.POST['title'], content=request.POST['content'], photo=request.FILES['photo'])
        upload.save()
        context = {"upload" : upload}

    return render(request, "fileupload.html", context)



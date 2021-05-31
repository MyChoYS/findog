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
from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.parsers import JSONParser

from frame.db import lostdoglistDb
from frame.login.db import MemberDb
from findog.models import dogcenter
from findog.models import missingdog
from findog.models import findingdog
from findog.models import dogbreed
from findog.models import mydog
from findog.models import member
from findog.models import UploadModel
from datetime import datetime

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
    return render(request, 'shelter/dogcenter.html', context)

#파일업로드
#파일업로드
def missingdog_upload(request) :
    context = None
    if request.method == 'POST' :
        #request.FILES['photo'] #분류 결과를 낸 후에
        #dogbreeds = 말티즈 #변수명에 담아서 밑에 upload의 dogbreed_id = 변수명 으로 저장!
        upload = missingdog(member_id_id=request.session['member_id'], dogbreed_id='Shih-Tzu',
                            title=request.POST['title'], findplace=request.POST['findplace'],
                            cellphone=request.POST['cellphone'], explanation=request.POST['content'],
                            img=request.FILES['photo'],
                            findtime=datetime.now().strftime('%Y%m%d%H%H%S'))
        upload.save()
        context = {"upload" : upload, }
    return render(request, "fileupload.html", context)


def findingdog_upload(request) :
    context = None
    if request.method == 'POST' :

        upload = findingdog(member_id_id = request.session['member_id'],dogbreed_id = 'Shih-Tzu',title = request.POST['title'], lostplace = request.POST['findplace'],
                            cellphone = request.POST['cellphone'],explanation=request.POST['content'], img = request.FILES['photo'],
                            losttime = datetime.now().strftime('%Y%m%d%H%H%S'))
        upload.save()
        context = {"upload" : upload,}
    return render(request, "fileupload2.html", context)

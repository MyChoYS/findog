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
    lastdog = lostdoglist.last()
    now = datetime.now()
    lostdogcount = lostdoglist.count()
    context = {
        'lostdoglist' : lostdoglist, 'lastdog' : lastdog, 'now' : now , 'lostdogcount' : lostdogcount
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


# login 관련
def login(request) :
    return render(request, 'login.html');

def login_register(request) :
    return render(request, 'login_register.html')


def loginimpl(request) :
    lostdoglist = missingdog.objects.all()

    member_id = request.POST['member_id']
    member_password = request.POST['member_pwd']
    #review = Academy_review.objects.get(pk=pk)
    try :
        #member = MemberDb().selectid(member_id);
        members = member.objects.get(id=member_id);
        if member_password == members.password :
            request.session['member_id'] = member_id
            request.session['member_name'] = members.name
            context = {
                'lostdoglist': lostdoglist,
                'login' : 'success',
                'member_name' : members.name
            };
        else :
            raise Exception
    except :
        context = {
            'lostdoglist': lostdoglist,
            'login' : 'fail',
            'message' : '로그인 실패',
        }
        return render(request, 'login.html', context)
    return render(request, 'main_board.html', context)

def login_registerimpl(request) :
    member_id = request.POST['member_id']
    member_pwd_1 = request.POST['member_pwd_1']
    member_pwd_2 = request.POST['member_pwd_2']
    member_name = request.POST['member_name']
    member_home = request.POST['member_home']
    member_cellphone = request.POST['member_cellphone']

    if member_pwd_1 != member_pwd_2 :
        context = {
            'message' : '회원가입 실패'
        };
        return render(request, 'login_register.html', context);
    else :
        try :
            #member().insert(member_id, member_name, member_pwd_1, member_home, member_cellphone);
            members = member(id=member_id, name = member_name, password = member_pwd_1, home = member_home, cellphone = member_cellphone )
            members.save()
        except :
            context = {
                'message' : '회원가입 실패'
            };
            return render(request, 'login_register.html', context);
        context = {
            'login' : 'success'
        };
        request.session['member_id'] = member_id
        request.session['member_name'] = member_name
        return render(request, 'main_board_detail.html', context)



def logout(request) :
    if 'member_id' in request.session :
        if request.session['member_id'] :
            del request.session['member_id']
    if 'member_id' in request.session :
        if request.session['member_name'] :
            del request.session['member_name']
    return redirect('base')


def androidlogin(request) :
    if request.method == 'POST' :
        print("request_ok");
        data = JSONParser().parse(request)
        print(data)
        member_id = data['member_id']
        member_pwd = data['member_pwd']

        members = member.objecs.get(id=member_id);
        print(members.member_pwd)
        print(member_pwd)

        if member_pwd == members.member_pwd :
            print('성공')
            return JsonResponse("ok", safe=False, json_dumps_params={'ensure_ascii':False})
        else :
            print('실패')
            return JsonResponse("fail", safe=False, json_dumps_params={'ensure_ascii':False})




#동물보호센터 현재위치 비교
def dogcenters(request) :
    doglocation = dogcenter.objects.all()

    context = {
        'doglocation': doglocation
    }
    return render(request, 'dogcenter.html', context)

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
        context = {"upload" : upload,}
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

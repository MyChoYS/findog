from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.parsers import JSONParser

from frame.db import lostdoglistDb
from frame.login.db import MemberDb




def base(request) :
    lostdoglist = lostdoglistDb().selectall()
    context = {
        'lostdoglist' : lostdoglist
    }
    return render(request, 'main.html', context);

def main_board(request) :
    lostdoglist = lostdoglistDb().selectall()
    context = {
        'lostdoglist': lostdoglist
    }
    return render(request, 'main_board.html', context);

def main_board_detail(request) :
    i_dogid = request.GET['i_dogid']
    item = lostdoglistDb().selectbyid(int(i_dogid))
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
    lostdoglist = lostdoglistDb().selectall()

    member_id = request.POST['member_id']
    member_pwd = request.POST['member_pwd']

    try :
        member = MemberDb().selectid(member_id);
        if member_pwd == member.member_pwd :
            request.session['member_id'] = member_id
            request.session['member_name'] = member.member_name
            context = {
                'lostdoglist': lostdoglist,
                'login' : 'success',
                'member_name' : member.member_name
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
            MemberDb().insert(member_id, member_name, member_pwd_1, member_home, member_cellphone);
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

        member = MemberDb().selectid(member_id);
        print(member.member_pwd)
        print(member_pwd)

        if member_pwd == member.member_pwd :
            print('성공')
            return JsonResponse("ok", safe=False, json_dumps_params={'ensure_ascii':False})
        else :
            print('실패')
            return JsonResponse("fail", safe=False, json_dumps_params={'ensure_ascii':False})








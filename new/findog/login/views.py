from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.parsers import JSONParser
from findog.models import missingdog
from findog.models import member



def login(request) :
    return render(request, 'login/login.html');

def login_register(request) :
    return render(request, 'login/login_register.html')

def loginimpl(request) :
    missingdoglist = missingdog.objects.all()

    member_id = request.POST['member_id']
    member_password = request.POST['member_pwd']
    try :
        members = member.objects.get(id=member_id);
        if member_password == members.password :
            request.session['member_id'] = member_id
            request.session['member_name'] = members.name
            context = {
                'missingdoglist': missingdoglist,
                'login' : 'success',
                'member_name' : members.name
            };
        else :
            raise Exception
    except :
        context = {
            'missingdoglist': missingdoglist,
            'login' : 'fail',
            'message' : '로그인 실패',
        }
        return render(request, 'login/login.html', context)
    return render(request, 'main/main.html', context)

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
        return render(request, 'login/login_register.html', context);
    else :
        try :
            #member().insert(member_id, member_name, member_pwd_1, member_home, member_cellphone);
            members = member(id=member_id, name = member_name, password = member_pwd_1, home = member_home, cellphone = member_cellphone )
            members.save()
        except :
            context = {
                'message' : '회원가입 실패'
            };
            return render(request, 'login/login_register.html', context);
        context = {
            'login' : 'success'
        };
        request.session['member_id'] = member_id
        request.session['member_name'] = member_name
        return render(request, 'main/main.html', context)



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







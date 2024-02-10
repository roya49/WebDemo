from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.utils import timezone
# Create your views here.
from .models import *

def login(request):
    # 用url访问是get请求,用提交按钮是post请求
    if request.method == "GET":  # 登录get请求
        return render(request, "login.html")
    # print(request.POST)  # 如果是POST请求，获取用户提交的数据
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = validate_user(username, password)
    if user:
        request.session['name'] = user.username
        request.session['id'] = user.job_number
        if user.role == 1:
            return redirect("/index/")  # 登录成功后跳转到指定网站
        return redirect("/stuff/")  # 登录成功后跳转到指定网站
    # return HttpResponse("登录失败")
    return render(request, 'login.html')

# 校验用户密码是否存在
def validate_user(username, password):
    try:
        # 根据用户名和密码查询用户
        user = User.objects.get(job_number=username, password=password)
        # print('根据用户名和密码查询用户:'+str(user))
        return user
    except User.DoesNotExist:
        return None


def index(request):
    if request.method == "GET":  # 登录get请求
        # name = User.username
        name = request.session.get('name')
        return render(request, 'index.html', {"name": name})
    print(request.POST)  # 如果是POST请求，获取用户提交的数据
    job_number = request.session.get('id')
    now_time = timezone.now()
    now_time_str = now_time.strftime("%Y-%m-%d %H:%M")
    if 'signIn' in request.POST:
        Work.objects.create(job_number=job_number, checkin_time=now_time_str)
        messages.success(request, "Sign in successful!")
        return render(request, 'index.html')
    if 'signOut' in request.POST:
        work = Work.objects.filter(job_number=job_number).order_by('checkin_time').reverse()[:1]
        work[0].checkout_time = now_time_str
        work[0].save()
        messages.success(request, "Sign out successful!")
        return render(request, 'index.html')

def stuff(request):
    name = request.session.get('name')
    return render(request, 'stuff.html', {"name": name})

def test(request):
    return render(request, 'base.html')

def work(request):
    name = request.session.get('name')
    return render(request, 'work.html', {"name": name})

def add(request):
    # 用url访问是get请求,用提交按钮是post请求
    if request.method == "GET":  # 登录get请求
        name = request.session.get('name')
        return render(request, "add.html", {"name": name})
    print(request.POST)  # 如果是POST请求，获取用户提交的数据
    job_number =request.POST.get("number")
    username = request.POST.get("name")
    password = request.POST.get("password")
    role = request.POST.get("role")
    User.objects.create(job_number=job_number, username=username, password=password, role=role)
    messages.success(request, "Add successful!")
    return render(request, 'work.html')

def stuffList(request):
    stuffs = User.objects.all()
    return render(request, 'stuff_list.html', {'stuffs': stuffs})
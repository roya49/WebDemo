from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def login(request):
    # 用url访问是get请求,用提交按钮是post请求
    if request.method == "GET":  # 登录get请求
        return render(request, "login.html")
    print(request.POST)  # 如果是POST请求，获取用户提交的数据
    username = request.POST.get("username")
    password = request.POST.get("password")
    if username == 'psya' and password == "2024":
        # return HttpResponse("登录成功")
        return redirect("/index/")  # 登录成功后跳转到指定网站

    # return HttpResponse("登录失败")
    return render(request, 'login.html')


def index(request):
    return render(request, 'index.html')

def test(request):
    return render(request, 'user.html')
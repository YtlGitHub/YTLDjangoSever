from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse  # 导入反向解析地址
# Create your views here.


def index(request):
    print(reverse("add"))  # 通过路由名称反向生成url请求地址
    print(reverse("index"))
    print(reverse("find", args=(100, 'lisi')))
    print(reverse("edit"))
    print(reverse("fun", args=(2021, 12)))
    # return redirect(reverse("fun", args=(2021, 12)))  # 路由重定向
    return HttpResponse("Hello World!")


def add(request):
    return HttpResponse("add....")


def find(request, sid=0, name=""):
    return HttpResponse("find....%d:%s"%(sid, name))


def update(request):
    return HttpResponse("update....")
    # raise Http404("修改页面不存在!")


def fun(request, yy=1000, mm=10):
    return HttpResponse(f"参数信息：{yy}年{mm}月")

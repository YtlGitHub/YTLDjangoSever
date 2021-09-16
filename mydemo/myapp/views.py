from django.shortcuts import render
from django.http import HttpResponse, Http404
# Create your views here.


def index(request):
    return HttpResponse("Hello World!")


def add(request):
    return HttpResponse("add....")


def find(request, sid=0, name=""):
    return HttpResponse(f"find....{sid}:{name}")


def update(request):
    # return HttpResponse("update....")
    raise Http404("修改页面不存在")


def fun(request, yy, mm):
    return HttpResponse(f"场数信息：{yy}年{mm}月")

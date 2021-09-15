from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("Hello World!")


def add(request):
    return HttpResponse("add....")


def find(request, sid):
    return HttpResponse(f"find....{sid}")


def update(request):
    return HttpResponse("update....")
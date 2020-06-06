from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    print(request)
    return HttpResponse('<h1>TEST-NEWS</h1>')

def test(request):
    return HttpResponse('<h1>TEST-PAGE</h1>')

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # print(dir(request))
    return HttpResponse('Добро пожаловать в ваш цифровой дневник!')


def test(request):
    return HttpResponse('<h1>тестовая страница<h1>')
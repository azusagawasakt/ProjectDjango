from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # print(dir(request))
    return HttpResponse('Добро пожаловать в ваш цифровой дневник!')


from django.shortcuts import render


def row(request):
    return render(request, 'main/index.html', {'user': request.user})


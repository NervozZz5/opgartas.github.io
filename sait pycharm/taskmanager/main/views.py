from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def Yan(request):
    return render(request, 'main/Yan.html')


def Danya(request):
    return render(request, 'main/Danya.html')


def Rij(request):
    return render(request, 'main/Rij.html')


def Sokrat(request):
    return render(request, 'main/Sokrat.html')


'''
Тут мы создаём функцию index
К которой обращаемся из файла urls в папке taskmanager

Так же создаём функцию about, к которой обращаемся из того же файла

Внутри функции индекс мы обращаемся к файлу разметки 
который находится в папке templates 
в котором в папке main находится наша разметка с названием index.html
чтобы указать путь в функции render мы указываем его так 
будто уже находимся в templates
Чтобы внутри html сделать тело 
! + Tab в файле
'''
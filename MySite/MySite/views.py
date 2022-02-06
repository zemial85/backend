import datetime
import random

from django.http import HttpResponse
from django.shortcuts import render


def hello_view(request):
    return render(request, 'test.html')


def empty_view(request):
    return HttpResponse('<h1> To jest pusta strona</h1>')


def date(request):
    obj = datetime.datetime.now()
    msg = f"Dziś jest: {obj:%Y-%m-%d} <br> Aktualna godzinia: {obj:%H-%M} "
    return HttpResponse(msg)


def data_view(request, data):
    return HttpResponse("Pierwszy widok!!! - int")


def data_str_view(request, data):
    return HttpResponse("Drugi widok!!! - str")


def random_data(request, n, start, stop):
        data = [str(random.randint(start, stop)) for i in range(n)]
        msg = ", ".join(data)
        return HttpResponse(f"Twoje {n} dla przedziału {start} - {stop} to: {msg}")


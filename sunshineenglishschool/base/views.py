from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "base/index.html")


def login(request):
    return render(request, "base/intro/login.html")


def intro01(request):
    return render(request, "base/intro/intro01.html")


def intro02(request):
    return render(request, "base/intro/intro02.html")


def intro03(request):
    return render(request, "base/intro/intro03.html")


def intro04(request):
    return render(request, "base/intro/intro04.html")


def intro05(request):
    return render(request, "base/intro/intro05.html")


def intro06(request):
    return render(request, "base/intro/intro06.html")


def intro07(request):
    return render(request, "base/intro/intro07.html")


def intro08(request):
    return render(request, "base/intro/intro08.html")


def intro09(request):
    return render(request, "base/intro/intro09.html")


def choosefamiliar(request):
    return render(request, "base/intro/choosefamiliar.html")


def hub(request):
    return render(request, "base/hub/hub.html")


def room(request):
    return render(request, "base/hub/room.html")


def london01(request):
    return render(request, "base/london/01.html")


def london02(request):
    return render(request, "base/london/02.html")


def london03(request):
    return render(request, "base/london/03.html")


def london04(request):
    return render(request, "base/london/04.html")


def london05(request):
    return render(request, "base/london/05.html")


def london06(request):
    return render(request, "base/london/06.html")


def london07(request):
    return render(request, "base/london/07.html")


def london08(request):
    return render(request, "base/london/08.html")


def london09(request):
    return render(request, "base/london/09.html")


def london10(request):
    return render(request, "base/london/10.html")


def london11(request):
    return render(request, "base/london/11.html")


def london12(request):
    return render(request, "base/london/12.html")


def london13(request):
    return render(request, "base/london/13.html")


def london14(request):
    return render(request, "base/london/14.html")
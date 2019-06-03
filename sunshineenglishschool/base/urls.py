from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),

    path("login", views.login, name='login'),
    path("intro01", views.intro01, name='intro01'),
    path("intro02", views.intro02, name='intro02'),
    path("intro03", views.intro03, name='intro03'),
    path("intro04", views.intro04, name='intro04'),
    path("intro05", views.intro05, name='intro05'),
    path("intro06", views.intro06, name='intro06'),
    path("intro07", views.intro07, name='intro07'),
    path("intro08", views.intro08, name='intro08'),
    path("intro09", views.intro09, name='intro09'),
    path("choosefamiliar", views.choosefamiliar, name='choosefamiliar'),

    path("hub", views.hub, name='hub'),
    path("room", views.room, name='room'),

    path("london01", views.london01, name='london01'),
    path("london02", views.london02, name='london02'),
    path("london03", views.london03, name='london03'),
    path("london04", views.london04, name='london04'),
    path("london05", views.london05, name='london05'),
    path("london06", views.london06, name='london06'),
    path("london07", views.london07, name='london07'),
    path("london08", views.london08, name='london08'),
    path("london09", views.london09, name='london09'),
    path("london10", views.london10, name='london10'),
    path("london11", views.london11, name='london11'),
    path("london12", views.london12, name='london12'),
    path("london13", views.london13, name='london13'),
    path("london14", views.london14, name='london14'),

    path("capetown01", views.capetown01, name='capetown01'),
    path("capetown02", views.capetown02, name='capetown02'),
    path("capetown03", views.capetown03, name='capetown03'),
    path("capetown04", views.capetown04, name='capetown04'),
    path("capetown05", views.capetown05, name='capetown05'),
    path("capetown06", views.capetown06, name='capetown06'),

    path("numidia01", views.numidia01, name='numidia01'),
    path("numidia02", views.numidia02, name='numidia02'),
    path("numidia03", views.numidia03, name='numidia03'),
    path("numidia04", views.numidia04, name='numidia04'),
    path("numidia05", views.numidia05, name='numidia05'),
    path("numidia06", views.numidia06, name='numidia06'),
    path("numidia07", views.numidia07, name='numidia07'),

    path("ethiopia01", views.ethiopia01, name='ethiopia01'),
    path("ethiopia02", views.ethiopia02, name='ethiopia02'),
    path("ethiopia03", views.ethiopia03, name='ethiopia03'),
    path("ethiopia04", views.ethiopia04, name='ethiopia04'),
    path("ethiopia05", views.ethiopia05, name='ethiopia05'),
    path("ethiopia06", views.ethiopia06, name='ethiopia06'),
    path("ethiopia07", views.ethiopia07, name='ethiopia07'),
    path("ethiopia08", views.ethiopia08, name='ethiopia08'),
    path("ethiopia09", views.ethiopia09, name='ethiopia09'),
    path("ethiopia10", views.ethiopia10, name='ethiopia10'),
    path("ethiopia11", views.ethiopia11, name='ethiopia11'),
    path("ethiopia12", views.ethiopia12, name='ethiopia12'),
    path("ethiopia13", views.ethiopia13, name='ethiopia13'),
    path("ethiopia14", views.ethiopia14, name='ethiopia14'),


    


]

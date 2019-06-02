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


]

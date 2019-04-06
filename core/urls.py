from django.urls import path
from . import views
from django.db import models
from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_all, name='create'),
    path('play/', views.play, name='play'),
    path('deck_detail/<slug:slug>', views.deck_detail, name='deck_detail'),
    path('card_detail/<slug:slug>', views.card_detail, name='card_detail'),
    path('random_play/', views.random_play, name='random_play'),
    path('get_cards/', views.get_cards, name='get_cards'),
    path('get_deck/<slug:slug>/', views.get_deck, name='get_deck'),
    path('play_deck/<slug:slug>/', views.play_deck, name='play_deck')
]

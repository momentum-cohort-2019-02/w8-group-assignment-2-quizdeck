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
    path('all_decks/', views.all_decks, name='all_decks'),
    path('my_decks/', views.my_decks, name='my_decks'),
    path('get_deck/<slug:slug>/', views.get_deck, name='get_deck'),
    path('play_deck/<slug:slug>/', views.play_deck, name='play_deck'),
    path('mark_card/', views.mark_card, name='mark_card'),
    path('users/<str:username>/', views.profile_page, name='profile_page'),
    path('users/<str:username>/decks/', views.profile_decks, name='profile_decks'),
    path('profile_get_decks/', views.profile_get_decks, name='profile_get_decks'),
    path('edit_deck/', views.edit_deck, name='edit_deck'),

]

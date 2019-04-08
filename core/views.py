
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, FormView, TemplateView
from django.views import generic
from django.contrib.auth.models import User
from django.http import JsonResponse
import json
from django.core.paginator import Paginator
from django.db.models import Q
from django.urls import reverse, reverse_lazy

# from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Our App imports:
from core.forms import CreateCardForm, NewDeckForm
from core.models import Card, Deck, Category, Score




# Create your views here.

def index(request):
    """View function for home page of site."""
    decks = Deck.objects.all()    
    # Render the HTML template index.html with the data in the context variable
    response = render(request, 'index.html', {
        "decks": decks,
    })
    return response


def play(request):
    """View function for starting a game."""
    response = render(request, 'play.html', {
    })
    return response

def deck_detail(request, slug):
    """View function for deck detail."""
    deck = Deck.objects.get(slug=slug)
    response = render(request, 'deck_detail.html', {
        "deck": deck
    })
    return response


def card_detail(request, slug):
    """View function for deck detail."""
    card = Card.objects.get(slug=slug)
    response = render(request, 'card_detail.html', {
        "card": card
    })
    return response

def random_play(request):
    return render(request, 'random_play.html',)

def play_deck(request, slug):
    deck = Deck.objects.get(slug=slug)
    return render(request, 'random_play.html', context= {"deck": deck})

def get_cards(request):
    cards = Card.objects.all()
    return JsonResponse({'cards': [(card.question, card.answer) for card in cards]})

def all_decks(request):
    decks = Deck.objects.all()
    paginator = Paginator(decks, 6)
    page = request.GET.get('page', 1)
    decks = paginator.get_page(page)
    return render(request, 'all_decks.html', {
        "decks": decks,
    })

def my_decks(request):
    decks = Deck.objects.all()
    paginator = Paginator(decks, 6)
    page = request.GET.get('page', 1)
    decks = paginator.get_page(page)
    return render(request, 'my_decks.html', {
        "decks": decks,
    })
    
    
def get_deck(request, slug):
    deck = Deck.objects.get(slug=slug)
    cards = deck.cards.all()
    return JsonResponse({'cards': [(card.question, card.answer) for card in cards]})

def create_all(request):
    
    if request.method == 'POST':
        deck_form = NewDeckForm(request.POST)
        card_form = CreateCardForm(request.POST)
        
        if deck_form.is_valid():
            deck = deck_form.save(commit=False)
            deck.author = request.user
            request.user.decks_owned.add(deck)
            deck.save()
            return redirect(deck.get_absolute_url())

        if card_form.is_valid():
            card = card_form.save(commit=False)
            card.author = request.user
            request.user.cards_owned.add()
            card.save()
            return redirect(card.get_absolute_url())

    else:
        card_form = CreateCardForm()
        deck_form = NewDeckForm()
            
    return render(request, 'create.html', {
        'card_form': card_form,
        'deck_form': deck_form,
    })

def mark_card(request):
    data = json.loads(request.body)
    card = Card.objects.get(Q(question=data['card_question'])|Q(answer=data['card_question']))
    score, created = request.user.score_set.get_or_create(card=card)
    if data['mark'] == 'right':
        score.right_answers += 1
        value = 1
        message = "Congrats!"
    else: 
        score.wrong_answers += 1
        value = 0
        message = "OK, will do!"
    score.save()

    return JsonResponse({'message': message, 'value': value})

def profile_page(request, username):
    user = User.objects.get(username=username)
    scores = Score.objects.filter(user=user)
    rights = 0
    total = 0
    for score in scores:
        rights += score.right_answers
        total += score.right_answers
        total += score.wrong_answers
    percent = int(100*(rights/total))
    return render(request, 'profile_page.html', {'user': user, 'percent': percent})

def profile_decks(request, username):
    user = User.objects.get(username=username)
    decks = user.decks_authored.all()
    paginator = Paginator(decks, 6)
    page = request.GET.get('page', 1)
    decks = paginator.get_page(page)
    return render(request, 'profile_decks.html', {'user': user, 'decks': decks})

def profile_get_decks(request):
    data = json.loads(request.body)
    user = User.objects.get(username=data['username'])
    if data['deckRel'] == 'authored':
        decks = user.decks_authored.all()
    elif data['deckRel'] == 'owned':
        decks = user.decks_owned.all()
        
    return render(request, 'partials/profile_get_decks.html', {'decks': decks})

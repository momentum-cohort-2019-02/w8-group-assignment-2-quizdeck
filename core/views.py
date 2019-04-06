
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.views import generic
from django.contrib.auth.models import User
from django.http import JsonResponse
import json
from django.core.paginator import Paginator

# from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required

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


def create(request):
    """View function for creating a card."""
    response = render(request, 'create.html', {
    })
    return response

def create_card(request):   
    """View function for CreateCardForm ."""

    if request.method == 'POST':
        form = CreateCardForm(request.POST
        )
        if form.is_valid():
            card = form.save(commit=False)
            card.save()
            return redirect(card.get_absolute_url())
        else:
            form = CreateCardForm()
        template = 'create_card.html'
        context = {'form': form}
        return render(request, template, context)
    
    form = CreateCardForm()
    template = 'create_card.html'
    context = {'form': form}
    return render(request, template, context)


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

# def create_card(request):   
#     """View function for CreateCardForm ."""

#     if request.method == 'POST':
#         form = CreateCardForm(request.POST
#         )
#         if form.is_valid():
#             card = form.save(commit=False)
#             card.save()
#             return redirect(card.get_absolute_url())
#         else:
#             form = CreateCardForm()
#         template = 'create_card.html'
#         context = {'form': form}
#         return render(request, template, context)
    
#     form = CreateCardForm()
#     template = 'create_card.html'
#     context = {'form': form}
#     return render(request, template, context)

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
    return render(request, 'my_decks.html', {
        "decks": decks,
    })
    
def new_deck(request):
    if request.method == 'POST':
        form = NewDeckForm(request.POST
        )
        if form.is_valid():
            deck = form.save(commit=False)
            deck.save()
            return redirect(deck.get_absolute_url())
        else:
            form = NewDeckForm()
        template = 'create-deck.html'
        context = {'form': form}
        return render(request, template, context)
    
    form = NewDeckForm()
    template = 'create-deck.html'
    context = {'form': form}
    return render(request, template, context)
    
def get_deck(request, slug):
    deck = Deck.objects.get(slug=slug)
    cards = deck.cards.all()
    return JsonResponse({'cards': [(card.question, card.answer) for card in cards]})

def mark_card(request):
    data = json.loads(request.body)
    card = Card.objects.get(question=data['card_question'])
    score, created = request.user.score_set.get_or_create(card=card)
    print(data)
    if data['mark'] == 'right':
        score.right_answers += 1
    else: 
        score.wrong_answers += 1
    score.save
    
    return JsonResponse({'ok': 'OK', 'right': score.right_answers, 'wrong': score.wrong_answers})

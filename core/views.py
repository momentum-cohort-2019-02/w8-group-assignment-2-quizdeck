from django.shortcuts import render
from .models import Deck
# from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required

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


def play(request):
    """View function for starting a game."""
    response = render(request, 'play.html', {
    })
    return response


def deck_detail(request, slug):
    """View function for deck detail."""
    deck = Deck.objects.filter(slug=slug)
    response = render(request, 'deck_detail.html', {
        "deck": deck
    })
    return response

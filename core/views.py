<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.views import generic
from django.contrib.auth.models import User

# Our App imports:
from core.forms import CreateCardForm
from core.models import Card, Deck, Category

=======
from django.shortcuts import render
from .models import Deck
>>>>>>> 2623ee3db2414718911f5e69de0f98195b1581a1

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

def create_card(request, slug):
    card = get_object_or_404(Deck, slug=slug)

    if request.method == 'POST':
        form = CreateCardForm(request.POST
        )
        if form.is_valid():
            card = form.save(commit=False)
            card.deck = Deckcard.save()
            return redirect(deck.get_absolute_url())
        else:
            form = CreateCardForm()
            template = 'core/create.html'
            context = {'form': form}
            return render(request, template, context)

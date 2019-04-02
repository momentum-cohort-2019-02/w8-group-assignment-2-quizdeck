from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.views import generic
from django.contrib.auth.models import User
from core.forms import CreateCardForm
from core.models import Card, Deck, Category

# Create your views here.

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
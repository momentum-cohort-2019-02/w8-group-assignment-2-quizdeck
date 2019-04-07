from django import forms
from .models import Card, Deck

class CreateCardForm(forms.ModelForm):

    class Meta:
        model = Card
        fields = ('question', 'answer', 'categories', 'decks',)

class NewDeckForm(forms.ModelForm):

    class Meta:
        model = Deck
        fields = ('title', 'description',)
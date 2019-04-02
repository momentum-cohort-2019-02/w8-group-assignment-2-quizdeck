from django.contrib import admin
from .models import Card, Deck, Category

# Register your models here.

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    """Class that creates the way Card info is displayed in Admin. Calls on Card Model"""
    list_display = (
        'question',
        'answer'
    )

@admin.register(Deck)
class DeckAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

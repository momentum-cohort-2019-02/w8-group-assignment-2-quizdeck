from django.contrib import admin
from .models import Card, Deck, Category

# Register your models here.

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    pass

@admin.register(Deck)
class DeckAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

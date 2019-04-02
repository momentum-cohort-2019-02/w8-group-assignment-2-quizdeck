from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Card(models.Model):
    """Model representing a Card."""

    # I went with question/answer instead of front/back
    question = models.TextField(max_length=255)
    answer = models.TextField(max_length=255)
    categories = models.ManyToManyField('Category', blank=True)
    decks = models.ManyToManyField('Deck')
    
    slug = models.SlugField(unique=True)

    def display_category(self):
        """Create a string for the Category. This is required to display category in Admin."""
        return ', '.join(category.name for category in self.category.all()[:3])
    display_category.short_description = 'category'

    def __str__(self):
        """String for representing the Model object."""
        return self.answer


class Deck(models.Model):
    """Model representing a Deck of cards."""

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True)
    
    
    def __str__(self):
        """String for representing the Model object."""
        return self.title


class Category(models.Model):
    """Model representing Categories"""
    
    name = models.CharField(max_length=100, help_text='Enter a Category (e.g. Python)')  
    slug = models.SlugField(unique=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """String for representing the Model object."""
        return self.name

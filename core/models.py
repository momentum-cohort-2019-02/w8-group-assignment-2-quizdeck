from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Card(models.Model):
    """Model representing a Card."""

    # I went with question/answer instead of front/back
    question = models.TextField(max_length=255)
    answer = models.TextField(max_length=255)
    categories = models.ManyToManyField('Category', blank=True)
    decks = models.ManyToManyField('Deck', related_name="cards")
    
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        self.set_slug()
        super().save(*args, **kwargs)
    

    def set_slug(self):
        if self.slug:
            return
        
        base_slug = slugify(self.question)
        slug = base_slug
        n = 0

        while Card.objects.filter(slug=slug).count():
            n += 1
            slug = base_slug + "-" + str(n)
        
        self.slug = slug

    def get_absolute_url(self):
        return reverse('card_detail', args=[str(self.slug)])

    def display_category(self):
        """Create a string for the Category. This is required to display category in Admin."""
        return ', '.join(category.name for category in self.category.all()[:3])
    display_category.short_description = 'category'

    def __str__(self):
        """String for representing the Model object."""
        return self.answer


class Deck(models.Model):
    """Model representing a Deck of cards."""

    #Need to make number of cards auto populate?
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True)

    card_count = models.CharField(max_length=100, null=True)
    difficulty = models.CharField(max_length=100, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    description = models.TextField(max_length=1000, default='N/A', null=True)

    
    def save(self, *args, **kwargs):
        self.set_slug()
        super().save(*args, **kwargs)
    
    def set_slug(self):
        if self.slug:
            return
        
        base_slug = slugify(self.title)
        slug = base_slug
        n = 0

        while Deck.objects.filter(slug=slug).count():
            n += 1
            slug = base_slug + "-" + str(n)
        
        self.slug = slug

    def get_absolute_url(self):
        return reverse('deck_detail', args=[str(self.slug)])

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



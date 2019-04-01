from django.db import models
import uuid

# Create your models here.
class Card(models.Model):
    """Model representing a Card."""

    question = models.TextField(max_length=200)
    answer = models.TextField(max_length=250)
    

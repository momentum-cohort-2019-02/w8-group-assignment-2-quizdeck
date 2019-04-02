from django.shortcuts import render
# from core.models import Create, Play


# Create your views here.
def index(request):
    """View function for home page of site."""
    cards = Card.objects.all()
    # Render the HTML template index.html with the data in the context variable
    response = render(request, 'index.html', {
        "cards": cards,
    })
    return response
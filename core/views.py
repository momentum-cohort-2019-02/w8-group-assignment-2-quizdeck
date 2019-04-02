from django.shortcuts import render


# Create your views here.
def index(request):
    """View function for home page of site."""
    # cards = Card.objects.all()
    # Render the HTML template index.html with the data in the context variable
    response = render(request, 'index.html', {
        # "cards": cards,
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
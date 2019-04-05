from quiz_deck.settings import *

import django_heroku

Debug = False

django_heroku.settings(locals())
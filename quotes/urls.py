from django.urls import path
from .views import get_random_quote

urlpatterns = [
    path('random-quote/', get_random_quote, name='random-quote'),
]

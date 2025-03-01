from django.urls import reverse_lazy

from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)

from .models import Joke
from .forms import JokeForm

class JokeCreateView(CreateView):
    model = Joke
    form_class = JokeForm


class JokeDeleteView(DeleteView):
    model = Joke
    form_class = JokeForm


class JokeDetailView(DetailView):
    model = Joke


class JokeListView(ListView):
    model = Joke


class JokeUpdateView(UpdateView):
    model = Joke
    fields = ['question', 'answer']
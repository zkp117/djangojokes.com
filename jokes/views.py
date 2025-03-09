from .models import Joke
from .forms import JokeForm

from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
class JokeCreateView(LoginRequiredMixin, CreateView):
    model = Joke
    form_class = JokeForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


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
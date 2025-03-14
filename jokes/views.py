import json
from .models import Joke, JokeVote
from .forms import JokeForm
from django.contrib import messages
from django.http import JsonResponse

from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
class JokeCreateView( SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Joke
    form_class = JokeForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class JokeDeleteView(UserPassesTestMixin, DeleteView):
    model = Joke
    success_url = reverse_lazy('jokes:list')

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        return result

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user
    
    def form_valid(self, form):
        messages.success(self.request, 'Joke deleted.')
        return super().form_valid(form)

class JokeDetailView(DetailView):
    model = Joke
class JokeListView(ListView):
    model = Joke
class JokeUpdateView( SuccessMessageMixin, UserPassesTestMixin, UpdateView):
    model = Joke
    form_class = JokeForm
    success_message = 'Joke Updated.'

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user

    fields = ['question', 'answer']

def vote(request, slug):
    user = request.user # logged in user or AnonymousUser
    joke = Joke.objects.get(slug=slug) # the joke instance
    data = json.loads(request.body) # data from the JavaScript

    # set simple variables.
    vote = data['vote'] # user's new vote.
    likes = data['likes'] # number of likes currently displayed on page
    dislikes = data['dislikes'] # number of dislikes currently displayed

    if user.is_anonymous: # user not logged in. Can't vote
        msg = 'Sorry, you have to be logged in to vote.'
    else: # user is logged in.
        if JokeVote.objects.filter(user=user, joke=joke).exists():
            # user already voted. Get user's past vote:
            joke_vote = JokeVote.objects.get(user=user, joke=joke)

            if joke_vote.vote == vote: # user's new vote is the same as past vote
                msg = 'Right. You told us already. Geez.'
            else: # user changed vote.
                joke_vote.vote = vote # update JokeVote instance
                joke_vote.save() 

                # set data to return to the browser
                if vote == -1:
                    likes -= 1
                    dislikes += 1
                    msg = "You changed your vote to dislike"
                else:
                    likes += 1
                    dislikes -= 1
                    msg = 'You changed your vote to like'
        else: # first time user is voting on this joke
            # create and save new vote
            joke_vote = JokeVote(user=user, joke=joke, vote=vote)
            joke_vote.save()

            # set data to return to the browser
            if vote == -1:
                dislikes += 1
                msg = "You voted to 'dislike' this joke"
            else:
                likes += 1
                msg = "You voted to 'like' this joke"

    # create object to return to browser
    response = {
        'msg': msg,
        'likes': likes,
        'dislikes': dislikes
    }
    return JsonResponse(response) # return object as JSON
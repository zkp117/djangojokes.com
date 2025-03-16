from django.contrib import admin
from .models import Category, Joke, JokeVote, Tag
from common.admin import DjangoJokesAdmin

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['category', 'created', 'updated']

    def get_readonly_fields(self, request, obj = None):
        if obj: # editing an existing object
            return ('slug', 'created', 'updated')
        return()
@admin.register(Joke)
class JokeAdmin(DjangoJokesAdmin):
    model = Joke
    
    # List Attributes
    date_hierarchy = 'updated'
    list_display = ['question', 'category', 'updated']
    list_filter = ['updated', 'category', 'tags']
    ordering = ['-updated']
    search_fields = ['question', 'answer']

    # Form Attributes
    autocomplete_fields = ['tags', 'user']
    radio_fields = { 'category': admin.HORIZONTAL}

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('slug', 'created', 'updated')

        return ()
    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag
    list_display = ['tag', 'created', 'updated']
    search_fields = ['tag']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing existing object
            return ('slug', 'created', 'updated')
        return()
    
@admin.register(JokeVote)
class JokeVoteAdmin(admin.ModelAdmin):
    model = JokeVote
    list_display = ['joke', 'user', 'vote']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('created', 'updated')
        return ()
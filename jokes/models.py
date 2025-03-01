from django.db import models
from django.urls import reverse
from common.utils.text import unique_slug

class Joke(models.Model):
    question = models.TextField(max_length=200)
    answer = models.TextField(max_length=100, blank=True)
    category = models.ForeignKey(
        'jokes.Category',  # Correct reference to Category model within the jokes app
        on_delete=models.PROTECT,
        null=True
    )
    slug = models.SlugField(
        max_length=50, unique=True, null=False, editable=False
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('jokes:detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug(self.question[:50], type(self))  # Generate the slug using unique_slug function
        super().save(*args, **kwargs)

    def __str__(self):
        return self.question


class Category(models.Model):
    category = models.CharField(max_length=50)
    slug = models.SlugField(
        max_length=50, unique=True, null=False, editable=False
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('jokes:category', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug(self.category[:50], type(self))  # Generate the slug using unique_slug function
        super().save(*args, **kwargs)

    def __str__(self):
        return self.category

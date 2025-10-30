from django.forms import ModelForm
from .models import Movie
from django import forms

# Create the form class.
class CreateMovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'director', 'release_year', 'rating', 'genre', 'duration']
        
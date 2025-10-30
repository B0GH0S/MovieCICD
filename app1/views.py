from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .forms import CreateMovieForm
from .models import Movie

def index(request):
    movies = Movie.objects.all().order_by('-id')
    return render(request, 'index.html', {'movies': movies})

def add_movie(request):
    if request.method == 'POST':
        form = CreateMovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateMovieForm()
    
    return render(request, 'add_movie.html', {'form': form})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movie_detail.html', {'movie': movie})

def edit_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        form = CreateMovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_detail', movie_id=movie.id)
    else:
        form = CreateMovieForm(instance=movie)
    
    return render(request, 'edit_movie.html', {'form': form, 'movie': movie})

def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        movie.delete()
        return redirect('index')
    
    return render(request, 'delete_movie.html', {'movie': movie})
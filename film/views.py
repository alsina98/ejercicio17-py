from django.shortcuts import render
from .models import Pelicula, Director, Tematica
from django.views import generic

def index(request):
    num_peliculas = Pelicula.objects.all().count()
    num_directores = Director.objects.all().count()
    return render(
        request,
        'index.html',
        context={
            'num_peliculas': num_peliculas,
            'num_directores': num_directores,
        }
    )

class FilmListView(generic.ListView):
    model = Pelicula

class DirectorListView(generic.ListView):
    model = Director
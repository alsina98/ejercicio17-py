from django.db import models
from django.urls import reverse

class Tematica(models.Model):
    name = models.CharField(max_length=70, help_text='Pon la tematica para la pelicula')

    def __str__(self):
        return self.name

class Pelicula(models.Model):
    title = models.CharField(max_length=200)
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Un resumen de la pelicula')
    tematica = models.ManyToManyField(Tematica, help_text='Selecciona una tematica para la pelicula')
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('film_detail', args=[str(self.id)])

class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)
from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=64)


class Movie(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    director = models.ForeignKey('Person', on_delete=models.CASCADE, related_name="movie_directors")
    actors = models.ManyToManyField('Person', through="Actor", related_name='movie_actors')
    year = models.IntegerField()


class Actor(models.Model):
    role = models.CharField(max_length=64)
    movies = models.ForeignKey(Movie, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

from django.test import TestCase
from rest_framework.test import APIClient
from .models import Person, Movie, Actor, MoviePerson
# Create your tests here.


class MovieTestCase(TestCase):

    def setUp(self):
        kacper = Person.objects.create(name='Kacper')
        baltazar = Person.objects.create(name='Baltazar')
        gabka = Person.objects.create(name='Gabka')

        mysterious = Movie.objects.create(
            title='tajemniczy smark na firance',
            year=1920,
            director=kacper
        )
        Actor.objects.create(movies=mysterious, person=gabka, role="Morskie stworzenie")

    def test_movie_get(self):

        client = APIClient()
        response = client.get('/movies/')
        assert response.status_code = 200

        content = response.data
        assert content[0]['title'] == "tajemniczy smark na firance"

    def test_post(self):
        client = APIClient()

        id = Person.objects.get(name='Kacper').id
        response = client.post('/movies/', {'title':'Tytuł',
                                            'year':1920,
                                            'director':id,
                                            'description':'Opis'})
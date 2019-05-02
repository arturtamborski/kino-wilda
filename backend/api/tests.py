from django.urls import reverse

from rest_framework import test

from backend.api import models
from backend.api import serializers


class Movie(test.APITestCase):
    client = test.RequestsClient()
    serializer = serializers.Movie
    model = serializer.Meta.model

    def setUp(self):
        self.model.objects.bulk_create([
            self.model(title='Bohemian Rhapsody', year=2016,
                       plot='The story of the legendary rock band '
                            'Queen and lead singer Freddie Mercury,'
                            'leading up to their famous performance '
                            'at Live Aid (1985).'),
            self.model(title='Incredibles 2', year=2017,
                       plot='The Incredibles hero family takes on '
                            'a new mission, which involves a change '
                            'in family roles: Bob Parr (Mr Incredible)'
                            ' must manage the house while his wife '
                            'Helen (Elastigirl) goes out to save the world.'),
            self.model(title='Venom', year=2018,
                       plot='A failed reporter is bonded to '
                            'an alien entity, one of many symbiotes '
                            'who have invaded Earth. But the being '
                            'takes a liking to Earth and decides '
                            'to protect it.')
        ])


class MovieTest(Movie):

    def test_get_all_movies(self):
        response = self.client.get(reverse('movies'))

        objects = self.model.objects.all()
        expected = self.serializer(objects, many=True).data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected)

    def test_get_all_movies_sorted_by_year_desc(self):
        params = {'sort': 'year'}
        response = self.client.get(reverse('movies'), params)

        objects = self.model.objects.all()
        expected = self.serializer(objects, many=True).data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected)

    def test_get_all_movies_sorted_by_year_asc(self):
        params = {'sort': '-year'}
        response = self.client.get(reverse('movies'), params)

        objects = self.model.objects.all().reverse()
        expected = self.serializer(objects, many=True).data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected)

    def test_post_new_movie(self):
        params = {'title': 'Star Wars'}
        response = self.client.post(reverse('movies'), params)

        objects = self.model.objects.latest('id')
        expected = self.serializer(objects).data
        del expected['id']

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), expected)

    def test_get_all_movies_after_update(self):
        response = self.client.get(reverse('movies'))

        objects = self.model.objects.all()
        expected = self.serializer(objects, many=True).data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected)


class Comment(test.APITestCase):
    client = test.RequestsClient()
    serializer = serializers.Comment
    model = serializer.Meta.model

    def setUp(self):

        # create movies
        Movie().setUp()

        self.model.objects.bulk_create([
            self.model(movie_id=models.Movie.objects.get(pk=1),
                       text='Great movie!'),
            self.model(movie_id=models.Movie.objects.get(pk=2),
                       text='Best movie!'),
            self.model(movie_id=models.Movie.objects.get(pk=2),
                       text='Good movie!'),
            self.model(movie_id=models.Movie.objects.get(pk=3),
                       text='Not so good movie'),
            self.model(movie_id=models.Movie.objects.get(pk=3),
                       text='Bad movie!'),
            self.model(movie_id=models.Movie.objects.get(pk=3),
                       text='Booo!'),
        ])


class CommentTest(Comment):

    def test_get_all_comments(self):
        response = self.client.get(reverse('comments'))

        objects = self.model.objects.all()
        expected = self.serializer(objects, many=True).data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected)

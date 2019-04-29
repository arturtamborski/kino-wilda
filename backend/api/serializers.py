from rest_framework import serializers

from . import models


class Movie(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = ('id', 'title', 'plot', 'year')


class Comment(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ('id', 'text')

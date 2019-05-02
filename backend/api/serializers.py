from rest_framework import serializers

from backend.api import models


class Movie(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = '__all__'


class Comment(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        exclude = ('date',)

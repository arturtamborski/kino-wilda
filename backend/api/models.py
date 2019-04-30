from django.db import models

from backend.api import querysets


class Movie(models.Model):
    title   = models.CharField(max_length=200)
    year    = models.IntegerField()
    plot    = models.TextField()

    objects = querysets.Movie.as_manager()

    class Meta:
        ordering = ('title',)


class Comment(models.Model):
    text    = models.CharField(max_length=200)
    date    = models.DateField()

    objects = querysets.Comment.as_manager()

from django.db import models

from backend.api import querysets


class Movie(models.Model):
    title = models.CharField(max_length=200, unique=True)
    year = models.PositiveSmallIntegerField()
    plot = models.TextField()

    objects = querysets.Movie.as_manager()

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title[:10]


class Comment(models.Model):
    text = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)

    objects = querysets.Comment.as_manager()

    class Meta:
        ordering = ('movie_id',)

    def __str__(self):
        return self.text[:10]

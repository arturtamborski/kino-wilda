from django.db import models


class Movie(models.Model):
    title   = models.CharField(max_length=200)
    year    = models.IntegerField()
    plot    = models.TextField()

    class Meta:
        ordering = ('title',)


class Comment(models.Model):
    text    = models.CharField(max_length=200)

from django.db import models

#cassandra imports
import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model


class MovieCas(Model):
    id = columns.Integer(required=False, primary_key=True)
    title = columns.Text(required=False)


class Movie(models.Model):
    dvd_title = models.TextField(null=True, blank=True)
    # studio = models.CharField(max_length=100, null=True, blank=True)
    released = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    sound = models.IntegerField(null=True, blank=True)
    versions = models.IntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    rating = models.CharField(max_length=20, null=True, blank=True)
    year = models.CharField(max_length=20, null=True, blank=True)
    # genre = models.CharField(max_length=20, null=True, blank=True)
    aspect = models.CharField(max_length=20, null=True, blank=True)
    upc = models.FloatField(null=True, blank=True)
    dvd_releasedate = models.CharField(max_length=20, null=True, blank=True)
    timestamp = models.CharField(max_length=20, null=True, blank=True)
    genre = models.ForeignKey('main.Genre', null=True, blank=True)

    def __unicode__(self):
        return self.dvd_title


class Genre(models.Model):
    genre = models.CharField(max_length=20, null=True, blank=True)


class Studio(models.Model):
    studio = models.CharField(max_length=100, null=True, blank=True)
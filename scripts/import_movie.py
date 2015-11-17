#!/usr/bin/env python

import csv
import sys
import os
from unidecode import unidecode

sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

import django
django.setup()

from main.models import Movie, MovieCas, Genre, Studio

from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from cassandra.cluster import Cluster

dir_name = os.path.dirname(os.path.abspath(__file__))
file_name = "dvd_csv.txt"

dvd_csv = os.path.join(dir_name, file_name)

csv_file = open(dvd_csv, 'r')

reader = csv.DictReader(csv_file)

# the Cassandra import script

# for row in reader:

#     dvd_name = unidecode(row['DVD_Title'])

#     print dvd_name

#     cluster = Cluster(['127.0.0.1'])
#     session = cluster.connect()
#     session.set_keyspace('movie_db')
#     movie = MovieCas(title=dvd_name)
#     movie.save()

#     cluster.shutdown()

    # csv_file.close()


for row in reader:

    #SQL model
        new_genre, created = Genre.objects.get_or_create(genre=row['Genre'])
        new_studio, created = Studio.objects.get_or_create(studio=row['Studio'])

        new_movie, created = Movie.objects.get_or_create(dvd_title=row['DVD_Title'])
        new_movie.status = row['Status']
        new_movie.price = row['Price']
        new_movie.rating = row['Rating']
        new_movie.release = row['DVD_ReleaseDate']

        new_movie.genre = new_genre
        new_movie.studio = new_studio

        try:
            new_movie.save()
        except Exception, e:
            print e 

    #Cassandra model
        cluster = Cluster(['127.0.0.1'])
        session = cluster.connect()
        session.set_keyspace('movie_db2')
        movie = MovieCas(dvd_title=unidecode(row['DVD_Title']))
        movie.id = new_movie.id
        movie.save()

        cluster.shutdown()

        # csv_file.close()

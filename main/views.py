from django.shortcuts import render, render_to_response
from django.template import RequestContext

from django.http import JsonResponse
from main.models import Movie, MovieCas 


def movie_detail(request, pk):
    
    context = {}

    movie = Movie.objects.get(pk=pk)


def movie_list_cas(request):

    context = {}

    movie_list = MovieCas.objects.all()


def movie_list_temp(request):

    context = {}

    movie_list = Movie.objects.all()[:5000]

    context['movie_list'] = movie_list

    return render_to_response('movie_list.html', context, context_instance=RequestContext(request))


def movie_list_mysql(request):

    context = {}

    movie_list = Movie.objects.using('mysql').all()[:5000]

    context['movie_list'] = movie_list

    return render_to_response('movie_list.html', context, context_instance=RequestContext(request))


def movie_list(request):

    page_number = request.GET.get('page', 100)

    if page_number != 100:
        start_number = page_number + 100
    else:
        start_number = 0

    movies = Movie.objects.all()[start_number:page_number]

    api_dict = {}

    movie_list = []

    api_dict['movies'] = movie_list

    for movie in movies:
        movie_list.append({'dvd_title': movie.dvd_title,
                           'studio': movie.studio,
                           'price': movie.price,
                           'rating': movie.rating,
                           'genre': movie.genre,
                           'dvd_releasedate': movie.dvd_releasedate,
                           })

    return JsonResponse(api_dict)


def movie_detail(request, pk):

    movie = Movie.objects.get(pk=pk)

    movie_Detail = {'title': movie.title,
                    'studio': movie.studio,
                    'price': movie.price,
                    'rating': movie.rating,
                    'genre': movie.genre,
                    'release': movie.release,
                    }

    return JsonResponse(movie_detail)


# curl -O http://www.trieuvan.com/apache/cassandra/3.0.0/apache-cassandra-3.0.0-bin.tar.gz

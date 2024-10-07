from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from movie_app.models import Director, Movie, Review
from movie_app.serializers import DirectorSerializer, MovieSerializer, ReviewSerializer

@api_view(['GET'])
def directors_list_api_view(request):
    directors = Director.objects.all()

    data = DirectorSerializer(instance=directors, many=True).data

    return Response(data=data)

@api_view(['GET'])
def movies_list_api_view(request):
    movies = Movie.objects.all()

    data = MovieSerializer(instance=movies, many=True).data

    return Response(data=data)


@api_view(['GET'])
def reviews_list_api_view(request):
    reviews = Review.objects.all()

    data = ReviewSerializer(instance=reviews, many=True).data

    return Response(data=data)

@api_view(['GET'])
def directors_detail_api_view(request, id ):
    directors = Director.objects.get(id=id)

    data = DirectorSerializer(instance=directors).data

    return Response(data=data)

@api_view(['GET'])
def movies_detail_api_view(request, id ):
    movies = Movie.objects.get(id=id)

    data = MovieSerializer(instance=movies).data

    return Response(data=data)


@api_view(['GET'])
def reviews_detail_api_view(request, id ):
    reviews = Review.objects.get(id=id)

    data = ReviewSerializer(instance=reviews).data

    return Response(data=data)



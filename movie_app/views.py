from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from movie_app.models import Director, Movie, Review
from movie_app.serializers import (DirectorSerializer, MovieSerializer,
                                   ReviewSerializer, DirectorValidateSerializer, MovieValidateSerializer,
                                   ReviewValidateSerializer)

@api_view(['GET', 'POST'])
def directors_list_create_api_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()

        data = DirectorSerializer(instance=directors, many=True).data

        return Response(data=data)


    elif request.method == 'POST':
        serializer = DirectorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)
        full_name = serializer.validated_data.get('full_name')

        director = Director.objects.create(
            full_name=full_name)

        return Response(data={'director_id': director.id},
                        status=status.HTTP_201_CREATED)



@api_view(['GET', 'POST'])
def movies_list_create_api_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        data = MovieSerializer(instance=movies, many=True).data
        return Response(data=data)

    elif request.method == 'POST':
        serializer = MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)
        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        director_id = serializer.validated_data.get('director_id')

        movie = Movie.objects.create(
            title=title,
            description=description,
            director_id=director_id
        )
        movie.save()
        return Response(data={'movie_id': movie.id},
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def reviews_list_create_api_view(request):
    if request.method == 'GET':

        reviews = Review.objects.all()
        data = ReviewSerializer(instance=reviews, many=True).data
        return Response(data=data)

    elif request.method == 'POST':
        serializer = ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)
        text = serializer.validated_data.get('text')
        stars = serializer.validated_data.get('stars')
        movie_id = serializer.validated_data.get('movie_id')
        review =  Review.objects.create(
            text=text,
            stars=stars,
            movie_id=movie_id
        )
        review.save()

        return Response(data={'review_id': review.id},
                        status=status.HTTP_201_CREATED)



@api_view(['GET', 'PUT', 'DELETE'])
def directors_detail_api_view(request, id):
    try:
        directors = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND,
                        data={'detail':'NOT FOUND'})

    if request.method == 'GET':
        data = DirectorSerializer(instance=directors).data
        return Response(data=data)

    elif request.method == 'PUT':
        serializer = DirectorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        directors.full_name = serializer.validated_data.get('full_name')
        directors.save()
        return Response(data=DirectorSerializer(instance=directors).data,
                        status= status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        directors.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def movies_detail_api_view(request, id):
    try:
        movies = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'detail': 'NOT FOUND'})
    if request.method == 'GET':
        data = MovieSerializer(instance=movies).data
        return Response(data=data)

    elif request.method == 'PUT':
        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        movies.title = serializer.validated_data.get('title')
        movies.description = serializer.validated_data.get('description')
        movies.director_id = serializer.validated_data.get('director_id')
        movies.save()
        return Response(data=DirectorSerializer(instance=movies).data,
                        status= status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def reviews_detail_api_view(request, id ):
    try:
        reviews = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'detail': 'NOT FOUND'})
    if request.method == 'GET':
        data = MovieSerializer(instance=reviews).data
        return Response(data=data)

    elif request.method == 'PUT':
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        reviews.text = serializer.validated_data.get('text')
        reviews.stars = serializer.validated_data.get('stars')
        reviews.movie_id = serializer.validated_data.get('movie_id')
        reviews.save()
        return Response(data=DirectorSerializer(instance=reviews).data,
                        status=status.HTTP_201_CREATED)


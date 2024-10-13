from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from movie_app.models import Director, Movie, Review
from movie_app.serializers import DirectorSerializer, MovieSerializer, ReviewSerializer

@api_view(['GET', 'POST'])
def directors_list_create_api_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()

        data = DirectorSerializer(instance=directors, many=True).data

        return Response(data=data)


    elif request.method == 'POST':
        full_name = request.data.get('full_name')

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
        title = request.data.get('title')
        description = request.data.get('description')
        director_id = request.data.get('director_id')

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

        text = request.data.get('text')
        stars = request.data.get('stars')
        movie_id = request.data.get('movie_id')
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
        directors.full_name = request.data.get('full_name')
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
        movies.title = request.data.get('title')
        movies.description = request.data.get('description')
        movies.director_id = request.data.get('director_id')
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
        reviews.text = request.data.get('text')
        reviews.stars = request.data.get('stars')
        reviews.movie_id = request.data.get('movie_id')
        reviews.save()
        return Response(data=DirectorSerializer(instance=reviews).data,
                        status=status.HTTP_201_CREATED)


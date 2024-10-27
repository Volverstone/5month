from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from movie_app.models import Director, Movie, Review
from movie_app.serializers import (DirectorSerializer, MovieSerializer,
                                   ReviewSerializer, DirectorValidateSerializer, MovieValidateSerializer,
                                   ReviewValidateSerializer)
from users.permissions import IsSuperUser
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'total': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
        })

class DirectorListAPIView(generics.ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    pagination_class = PageNumberPagination
    
class DetailDirectorAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = 'id'

class MovieListAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, DirectortValiditySerializer, ReviewValiditySerializer


class DirectorListAPIView(generics.ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

    def post(self, request, *args, **kwargs):
        validator = DirectortValiditySerializer(data=request.data)
        if not validator.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'error': validator.errors})
        name = validator.validated_data['name']
        Director.objects.create(name=name)
        return Response(status=status.HTTP_201_CREATED)


class DirectorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        name_detail = self.get_object()
        validator = DirectortValiditySerializer(data=request.data)
        if not validator.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'error': validator.errors})
        name_detail.name = validator.validated_data['name']
        name_detail.save()
        return Response(status=status.HTTP_200_OK)


class MovieListAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer



class MovieDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'


class ReviewListAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'


@api_view(['GET', 'POST'])
@permission_classes([IsSuperUser])
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


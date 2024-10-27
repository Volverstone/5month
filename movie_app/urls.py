from django.urls import path
from movie_app import views

urlpatterns = [
    path('movies/', views.movies_list_create_api_view),
    path('directors', views.directors_list_create_api_view),
    path('reviews/', views.reviews_list_create_api_view),
    path('directors/<int:id>/', views.directors_detail_api_view),
    path('reviews/<int:id>/', views.reviews_detail_api_view),
    path('movies/<int:id>/', views.movies_detail_api_view),
    path('movies/', views.MovieListAPIView.as_view(), name='movie_list'),
    path('movies/<int:id>/', views.MovieDetailAPIView.as_view(), name='movie_detail'),

    path('directors/', views.DirectorListAPIView.as_view(), name='director_list'),
    path('directors/<int:id>/', views.DirectorDetailAPIView.as_view(), name='director_detail'),

    path('reviews/', views.ReviewListAPIView.as_view(), name='review_list'),
    path('reviews/<int:id>/', views.ReviewDetailAPIView.as_view(), name='review_detail'),
    ]
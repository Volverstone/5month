from django.urls import path
from movie_app import views

urlpatterns = [
    path('movies/', views.movies_list_create_api_view),
    path('directors', views.directors_list_create_api_view),
    path('reviews/', views.reviews_list_create_api_view),
    path('directors/<int:id>/', views.directors_detail_api_view),
    path('reviews/<int:id>/', views.reviews_detail_api_view),
    path('movies/<int:id>/', views.movies_detail_api_view),
]
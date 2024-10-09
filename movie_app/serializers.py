from rest_framework import serializers
from movie_app.models import Director, Review, Movie

class DirectorSerializer(serializers.ModelSerializer):
    movies = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    review_star = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = '__all__'
        depth = 2

    def get_review_star(self, star):
        return star.review.stars if star.review else None



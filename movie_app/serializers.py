from rest_framework import serializers
from movie_app.models import Director, Review, Movie
from rest_framework.serializers import ValidationError

class DirectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
        depth = 2


class DirectorValidateSerializer(serializers.Serializer):
    full_name = serializers.CharField(required=True, min_length=5, max_length=100)


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    director_id= serializers.IntegerField()

    def director_validate(self, director_id):
        try:
            Review.objects.get(id=director_id)
        except:
            raise ValidationError('Director doesnt exist')
        return director_id

class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    stars = serializers.IntegerField()
    movie_id = serializers.IntegerField()

    def movie_validate(self, movie_id):
        try:
            Review.objects.get(id=movie_id)
        except:
            raise ValidationError('Movie doesnt exist')
        return movie_id






from django.contrib import admin
from movie_app.models import Director, Review, Movie


admin.site.register(Director)
admin.site.register(Review)
admin.site.register(Movie)

# Register your models here.

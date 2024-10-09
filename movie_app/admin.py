from django.contrib import admin
from movie_app.models import Director, Review, Movie


class ReviewInline(admin.StackedInline):
    model = Review
    extra = 1


class MovieAdmin(admin.ModelAdmin):
    inlines = [ReviewInline]

admin.site.register(Director)
admin.site.register(Review)
admin.site.register(Movie)

# Register your models here.

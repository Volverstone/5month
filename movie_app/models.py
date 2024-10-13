from django.db import models

# Create your models here.
class Director(models.Model):
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.full_name}"


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE,null=True, blank=True )
    def __str__(self):
        return f"{self.title}"

STAR_CHOICES = (
    (i, '*' * i) for i in range(1,6)
)

class Review(models.Model):
    text = models.TextField(null=True, blank=True)
    stars = models.IntegerField(default=5, choices=STAR_CHOICES)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,null=True, blank=True)
    def __str__(self):
        return f"{self.text}"



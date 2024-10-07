from django.db import models

# Create your models here.
class Director(models.Model):
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.full_name}"
class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    duration = models.FloatField(default=0)
    director = models.ForeignKey(Director, on_delete=models.CASCADE,null=True, blank=True )
    def __str__(self):
        return f"{self.title}"
class Review(models.Model):
    text = models.TextField(null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f"{self.text}"
from django.db import models


# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    release_date = models.DateTimeField()
    likes = models.CharField(max_length=255)  # ! is there a way to make it unlimited?


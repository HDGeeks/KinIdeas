from pyexpat import model
from django.db import models
from django.utils import timezone
from core.settings import MEDIA_ROOT

# Create your models here.

def user_directory_path(self, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(self.album_artist.id, filename)


class Genre(models.model):
    """    YEAR_IN_SCHOOL_CHOICES = [
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
    ('GR', 'Graduate'),
    ] """
    genre_id=models.IntegerField(max_lengt=50 ,primary_key=True)
    genre_name=models.CharField(max_length=50)
    genre_cover=models.ImageField()
    genre_description=models.CharField(max_length=100)

class Artist(models.model):
    artist_id=models.IntegerField(max_lengt=50 ,primary_key=True)
    artist_name=models.CharField(max_length=50)
    artist_cover=models.ImageField()
    artist_description=models.CharField(max_length=100)
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)



class Album(models.model):
    genre_id=Genre.genre_id
    artist_id=Artist.artist_id
    album_id=models.IntegerField(max_lengt=50,primary_key=True)
    album_name=models.CharField(max_length=50)
    album_cover=models.ImageField()
    album_description=models.CharField(max_length=100)
    album_release_date=models.DateTimeField

class Track(models.Model):
    track_id=models.IntegerField(max_length=50 , primary_key=True)
    genre_id=Genre.genre_id
    artist_id=Artist.artist_id
    album_id=Album.album_id
    album_cover=Album.album_cover
    track_description=models.CharField(max_length=100)
    track_name = models.CharField(max_length=30)


   

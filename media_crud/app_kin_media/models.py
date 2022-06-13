from pyexpat import model
from django.db import models
from django.utils import timezone
from core.settings import MEDIA_ROOT

# Create your models here.

def user_directory_path(self, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(self.album_artist.id, filename)


class Genre(models.model):
    """ CATEGORY = (  ('solo', 'solo'),
                ('jazz', 'jazz'),
                ('ambasel','ambasel'),
                ('bati', 'bati')
                ) """
    genre_id=models.IntegerField(max_lengt=50 ,primary_key=True ,blank=False ,null=False)
    genre_name=models.CharField(max_length=50 ,blank=False ,null=False)
    #genre_cover=models.ImageField()
    genre_description=models.CharField(max_length=100)

class Artist(models.model):
    artist_id=models.IntegerField(max_lengt=50 ,primary_key=True ,blank=False ,null=False)
    artist_name=models.CharField(max_length=50 ,blank=False ,null=False)
    artist_cover=models.ImageField()
    artist_description=models.CharField(max_length=100 ,null=False)
    #genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
    genre_id=models.ManyToManyRel(Genre, on_delete=models.CASCADE)



class Album(models.model):
    album_id=models.IntegerField(max_lengt=50,primary_key=True ,blank=False ,null=False)
    album_name=models.CharField(max_length=50 ,blank=False ,null=False) 
    album_cover=models.ImageField()
    album_description=models.CharField(max_length=100 ,null=False) 
    album_release_date=models.DateTimeField
    #artist_id= models.ForeignKey(Artist, on_delete=models.CASCADE)
    #genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
    genre_id=models.ManyToManyRel(Genre, on_delete=models.CASCADE)
    artist_id=models.ManyToOneRel(Artist, on_delete=models.CASCADE)

    
class Track(models.Model):
    track_id=models.IntegerField(max_length=50 , primary_key=True ,blank=False ,null=False)
    track_name = models.CharField(max_length=30 ,blank=False ,null=False)
    track_description=models.CharField(max_length=100 ,null=False)
    track_release_date=models.DateTimeField
    #genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
    #artist_id= models.ForeignKey(Artist, on_delete=models.CASCADE)
    #album_id= models.ForeignKey(Album, on_delete=models.CASCADE)
    genre_id=models.ManyToManyRel(Genre, on_delete=models.CASCADE)
    artist_id=models.ManyToOneRel(Artist, on_delete=models.CASCADE)
    album_id=models.ManyToOneRel(Album, on_delete=models.CASCADE, null=True, blank=True)
    album_cover=Album.album_cover (null=True, blank=True)
    track_audio=models.FilePathField





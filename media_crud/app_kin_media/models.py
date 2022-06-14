from pyexpat import model
from django.db import models
from django.utils import timezone
from core.settings import MEDIA_ROOT
from django.utils.translation import gettext_lazy as _

# Create your models here.

""" def user_directory_path(self, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(self.album_artist.id, filename) """

 


class Artist(models.model):

    artist_id=models.AutoField(max_lengt=255 , primary_key=True)
    artist_name=models.CharField(max_length=255 ,default=_(
    "unknown"),null=False ,blank=False)
    artist_photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    artist_description=models.CharField(max_length=100)

    class Meta:
        verbose_name = _("Artist")
        verbose_name_plural = _("Artists")
        ordering = ['id']
  

    def __str__(self):
        return self.artist_name



class Album(models.model):

    Genre= (
        (0, _('reggea')),
        (1, _('hip-hop')),
        (2, _('pop')),
        (3, _('soul')),
        (4, _('RnB'))
    )
    album_id=models.AutoField(max_lengt=50,primary_key=True)
    artist = models.ForeignKey(
        Artist , default=1 , on_delete=models.DO_NOTHING)
    album_genre = models.IntegerField(
        choices=Genre, default=0, verbose_name=_("Difficulty"))
  
    album_name=models.CharField(max_length=255 , null=False , blank= False ,default='unknown')
    album_cover = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    album_description=models.CharField(max_length=255 , null=False , blank=False ,default= "name")
    album_release_date=models.DateTimeField(auto_now_add=True,)

    

    class Meta:
        verbose_name = _("Album")
        verbose_name_plural = _("Albums")
        ordering = ['id']

    def __str__(self):
        return self.album_name , self.album_release_date

class Track(models.Model):

    track_id=models.AutoField(primary_key=True)
    artist = models.ForeignKey(
        Artist , default=1 , on_delete=models.DO_NOTHING)
    album = models.ForeignKey(
        Album, default=1 , on_delete=models.DO_NOTHING)
    album_cover = models.ForeignKey(
        Album , default=1 , on_delete=models.DO_NOTHING)
    track_description=models.CharField(max_length=100)
    track_name= models.CharField(max_length=50 , null=False ,blank=False)
    track_file = models.FileField(upload_to='' , null=True)

    class Meta:
        verbose_name = _("Track")
        verbose_name_plural = _("Tracks")
        ordering = ['id']


    def __str__(self):
        return self.track_name ,self.track_file ,self.track_file
        


   

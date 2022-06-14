from rest_framework import serializers
from .models import Genre ,Artist ,Album , Track


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ("artist_id" , "arists_name", "genre_cover")

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ("artist_id" , "arists_name", "genre_cover")


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ("artist_id" , "arists_name", "genre_cover")
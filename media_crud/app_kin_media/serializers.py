from rest_framework import serializers
from .models import Artist ,Album ,Track




from .models import Artist, Album, Track

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ("track_id" , "artist", "album ", "track_description", "track_name", "track_file", "duration",)

class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True)

    class Meta:
        model = Album
        fields = ("album_id" , "artist", " album_genre","album_name","album_cover", "album_description", "album_release_date")

    def create(self, validated_data):
        tracks_data = validated_data.pop('tracks')
        album = Album.objects.create(**validated_data)
        for track_data in tracks_data:
            Track.objects.create(album=album, **track_data)
        return album

class ArtistSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True)

    class Meta:
        model = Artist
        fields = ("artist_id" , "arists_name", "artist_photo", "artist_description")

    def create(self, validated_data):
        albums_data = validated_data.pop('albums')
        artist = Artist.objects.create(**validated_data)
        for album_data in albums_data:
            Album.objects.create(artist=artist, **album_data)
        return artist

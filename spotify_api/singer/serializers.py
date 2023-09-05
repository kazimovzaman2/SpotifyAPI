import os
from rest_framework.serializers import ModelSerializer, ValidationError

from spotify_api.users.serializers import CreateUserSerializer, UserSerializer
from spotify_api.singer.models import Playlist, Singer, Song


class SingerReadUpdateSerializer(ModelSerializer):
    """Serializer for Singer model"""

    user = UserSerializer()

    class Meta:
        model = Singer
        fields = ("id", "user", "profile_image")

    def update(self, instance, validated_data):
        user_data = validated_data.get('user', {})
        if user_data:
            user = instance.user
            user_serializer = UserSerializer(user, data=user_data)
            user_serializer.is_valid(raise_exception=True)
            user_serializer.save()

        instance.profile_image = validated_data.get('profile_image', instance.profile_image)
        instance.save()

        return instance

class SingerCreateSerializer(ModelSerializer):
    """Serializer for Singer model"""

    user = CreateUserSerializer()

    class Meta:
        model = Singer
        fields = ("user", "profile_image")
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = CreateUserSerializer.create(CreateUserSerializer(), validated_data=user_data)
        singer = Singer.objects.create(user=user, **validated_data)
        return singer


class SongSerializer(ModelSerializer):
    """Serializer for Song model"""

    singer = SingerReadUpdateSerializer(read_only=True)

    class Meta:
        model = Song
        fields = ("id", "singer", "title", "audio", "image", "created_at", "updated_at")
        read_only_fields = ("id", "created_at", "updated_at")

    def validate_audio(self, audio):
        allowed_extensions = ['.mp3', '.wav', '.m4a', '.mp4', '.ogg', '.flac']
        file_extension = os.path.splitext(audio.name)[1].lower()
        if file_extension not in allowed_extensions:
            raise ValidationError(f"File with extension {file_extension} is not allowed.")

        return audio

    def create(self, validated_data):
        singer = self.context['request'].user.singer
        song = Song.objects.create(singer=singer, **validated_data)
        return song

class PlaylistSerializer(ModelSerializer):
    """Serializer for Playlist model"""

    singer = SingerReadUpdateSerializer(read_only=True)

    class Meta:
        model = Playlist
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")

    def create(self, validated_data):
        singer = self.context['request'].user.singer
        songs_data = validated_data.pop('songs', [])
        playlist = Playlist.objects.create(singer=singer, **validated_data)
        playlist.songs.set(songs_data)
        return playlist

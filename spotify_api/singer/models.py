from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

class Singer(models.Model):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE, related_name='singer')
    profile_image = models.ImageField(upload_to='singer/profile_image', blank=True)

    class Meta:
        verbose_name = 'singer'
        verbose_name_plural = 'singers'

    
    def __str__(self) -> str:
        return self.user.username

    def __repr__(self) -> str:
        return f'<Singer {self.user.username}>'

class Song(models.Model):
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='songs')
    title = models.CharField(max_length=100)
    audio = models.FileField(
        upload_to='song/audio',
        validators=[
            FileExtensionValidator(['mp3', 'wav', 'm4a', 'mp4', 'ogg', 'flac']),
        ],
    )
    image = models.ImageField(upload_to='song/image', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'song'
        verbose_name_plural = 'songs'

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return f'<Song {self.title}>'

class Playlist(models.Model):
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='playlists')
    title = models.CharField(max_length=100)
    songs = models.ManyToManyField(Song, related_name='playlists')
    image = models.ImageField(upload_to='playlist/image', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'playlist'
        verbose_name_plural = 'playlists'

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return f'<Playlist {self.title}>'

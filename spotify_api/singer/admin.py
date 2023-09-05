from django.contrib import admin
from .models import Singer, Song, Playlist

# Register your models here.
@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display = ['user',]

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['title', 'singer',]

@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ['title', 'singer',]
# Generated by Django 4.2.1 on 2023-09-05 03:27

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('singer', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='playlist',
            options={'verbose_name': 'playlist', 'verbose_name_plural': 'playlists'},
        ),
        migrations.AlterModelOptions(
            name='singer',
            options={'verbose_name': 'singer', 'verbose_name_plural': 'singers'},
        ),
        migrations.AlterModelOptions(
            name='song',
            options={'verbose_name': 'song', 'verbose_name_plural': 'songs'},
        ),
        migrations.AlterField(
            model_name='playlist',
            name='image',
            field=models.ImageField(blank=True, upload_to='playlist/image'),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='singer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playlists', to='singer.singer'),
        ),
        migrations.AlterField(
            model_name='singer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='singer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='song',
            name='audio',
            field=models.FileField(upload_to='song/audio', validators=[django.core.validators.FileExtensionValidator(['mp3', 'wav', 'm4a', 'mp4', 'ogg', 'flac'])]),
        ),
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.ImageField(blank=True, upload_to='song/image'),
        ),
        migrations.AlterField(
            model_name='song',
            name='singer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='singer.singer'),
        ),
    ]

from django.db import models
from django.utils.text import slugify

class Album(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
class Genre(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Mix(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    episode = models.CharField(max_length=3, blank=True, null=True)
    color = models.CharField(max_length=15, blank=True, null=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, blank=True, null=True)
    stream_link = models.TextField(blank=True, null=True)
    is_popular = models.BooleanField(default=False, blank=True, null=True)
    featured_artists = models.TextField(blank=True, null=True)
    similar_mixes = models.TextField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    play_count = models.PositiveIntegerField(default=0, blank=True, null=True)
    download_count = models.PositiveIntegerField(default=0, blank=True, null=True)
    reshare_count = models.PositiveIntegerField(default=0, blank=True, null=True)
    like_count = models.PositiveIntegerField(default=0, blank=True, null=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title

class Playlist(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    episode = models.CharField(max_length=3, blank=True, null=True)
    color = models.CharField(max_length=15, blank=True, null=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, blank=True, null=True)
    stream_link = models.TextField(blank=True, null=True)
    is_popular = models.BooleanField(default=False, blank=True, null=True)
    featured_artists = models.TextField(blank=True, null=True)
    similar_mixes = models.TextField(blank=True, null=True)
    similar_playlists = models.TextField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title
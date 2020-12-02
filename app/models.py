from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', default='images/default.png')
    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)


class Genre(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    text = models.TextField(max_length=400)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(default=timezone.now)
    bio = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Song(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    publish_date = models.DateField(default=timezone.now)
    image = models.ImageField(upload_to='images')
    mp3 = models.FileField(upload_to='mp3')
    liked = models.ManyToManyField(User, blank=True)

    class Meta:
        ordering = ['author','title']

    def __str__(self):
        return self.title


class Playlist(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    songs = models.ManyToManyField(Song, blank=True)
    text = models.TextField(max_length=400)
    image = models.ImageField(upload_to='images')
    liked = models.ManyToManyField(User, blank=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Album(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    songs = models.ManyToManyField(Song, blank=True)
    publish_date = models.DateField(default=timezone.now)
    image = models.ImageField(upload_to='images')
    liked = models.ManyToManyField(User, blank=True)

    class Meta:
        ordering = ['author','title']

    def __str__(self):
        return self.title

















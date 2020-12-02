from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import *


def index(request):
    songs = Song.objects.order_by('author','title')
    latest_songs = Song.objects.all()
    albums = Album.objects.order_by('author','title')
    playlists = Playlist.objects.order_by('title')
    genres = Genre.objects.order_by('title')
    authors = Author.objects.order_by('name')
    return render(request, "app/index.html", {'songs': songs, 'albums': albums, 'playlists': playlists, 'genres': genres, 'authors': authors, 'latest_songs': latest_songs})


def genre_list(request):
    genres = Genre.objects.order_by('title')
    return render(request, 'app/genre_list.html', {'genres': genres})


def author_list(request):
    authors = Author.objects.order_by('name')
    return render(request, 'app/author_list.html', {'authors': authors})


def song_list(request):
    songs = Song.objects.order_by('author','title')
    return render(request, 'app/song_list.html', {'songs': songs})


def playlist_list(request):
    playlists = Playlist.objects.order_by('title')
    return render(request, 'app/playlist_list.html', {'playlists': playlists})


def album_list(request):
    albums = Album.objects.order_by('author','title')
    return render(request, 'app/album_list.html', {'albums': albums})


def genre_detail(request, pk):
    genre = Genre.objects.get(pk=pk)
    songs = Song.objects.filter(genre=genre)
    return render(request, 'app/genre_detail.html', {'genre':genre,'songs':songs})


def author_detail(request, pk):
    author = Author.objects.get(pk=pk)
    songs = Song.objects.filter(author=author)
    albums = Album.objects.filter(author=author)
    return render(request, 'app/author_detail.html', {'author':author,'songs':songs,'albums':albums})


def song_detail(request, pk):
    song = Song.objects.get(pk=pk)
    if song.liked.filter(id=request.user.id).exists():
        is_liked = True
    else:
        is_liked = False
    if request.method == 'POST':
        form = SongForm(request.user, request.POST)
        if form.is_valid():
            playlist = form.cleaned_data.get('playlist')
            playlist.songs.add(song)
            return HttpResponseRedirect(reverse('playlist_detail', args=[str(playlist.id)]))
    else:
        form = SongForm(request.user)
    return render(request, 'app/song_detail.html', {'song':song,'is_liked':is_liked,'form':form})


def playlist_detail(request, pk):
    playlist = Playlist.objects.get(pk=pk)
    if playlist.author.id == request.user.id:
        is_my = True
    else:
        is_my = False
    if playlist.liked.filter(id=request.user.id).exists():
        is_liked = True
    else:
        is_liked = False
    return render(request, 'app/playlist_detail.html', {'playlist':playlist,'is_liked':is_liked,'is_my':is_my})


def album_detail(request, pk):
    album = Album.objects.get(pk=pk)
    if album.liked.filter(id=request.user.id).exists():
        is_liked = True
    else:
        is_liked = False
    return render(request, 'app/album_detail.html', {'album':album,'is_liked':is_liked})


def profile(request):
    liked_songs = Song.objects.filter(liked=request.user.id)
    liked_albums = Album.objects.filter(liked=request.user.id)
    liked_playlists = Playlist.objects.filter(liked=request.user.id)
    my_playlists = Playlist.objects.filter(author=request.user.id)
    if request.method == 'POST':
        form = PlaylistForm(request.user, request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../profile/')
    if request.method == 'post' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        userprofile.image = ImageFile(f)
        UserProfile.save()
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    else:
        form = PlaylistForm(request.user, initial={'author': request.user})
        form.fields['author'].widget = forms.HiddenInput()
    return render(request, "app/profile.html", {'liked_songs':liked_songs,'liked_albums':liked_albums,'liked_playlists':liked_playlists,'my_playlists':my_playlists,'form':form})


def like_song(request, pk):
    song = Song.objects.get(id=pk)
    if song.liked.filter(id=request.user.id).exists():
        song.liked.remove(request.user)
    else:
        song.liked.add(request.user)
    return HttpResponseRedirect(reverse('song_detail', args=[str(pk)]))


def like_album(request, pk):
    album = Album.objects.get(id=pk)
    if album.liked.filter(id=request.user.id).exists():
        album.liked.remove(request.user)
    else:
        album.liked.add(request.user)
    return HttpResponseRedirect(reverse('album_detail', args=[str(pk)]))


def like_playlist(request, pk):
    playlist = Playlist.objects.get(id=pk)
    if playlist.liked.filter(id=request.user.id).exists():
        playlist.liked.remove(request.user)
    else:
        playlist.liked.add(request.user)
    return HttpResponseRedirect(reverse('playlist_detail', args=[str(pk)]))


def create_playlist(request):
    playlist = Playlist(author=UserProfile, title="test", text="text")
    playlist.save()


def delete_playlist(request, pk):
    playlist = Playlist.objects.get(pk=pk)
    if playlist.author.id == request.user.id:
        playlist.delete()
    return HttpResponseRedirect('../playlists/')


def delete_song_from_playlist(request, pk1, pk2):
    playlist = Playlist.objects.get(id=pk2)
    playlist.songs.remove(pk1)
    return HttpResponseRedirect(reverse('playlist_detail', args=[str(pk2)]))


def search(request):
    query = request.GET.get('text')
    songs = Song.objects.filter(title__icontains=query)
    albums = Album.objects.filter(title__icontains=query)
    playlists = Playlist.objects.filter(title__icontains=query)
    genres = Genre.objects.filter(title__icontains=query)
    authors = Author.objects.filter(name__icontains=query)
    return render(request, "app/search.html",{'songs': songs, 'albums': albums, 'playlists': playlists,'genres': genres, 'authors': authors})


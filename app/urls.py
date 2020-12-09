from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('', views.index, name='index'),
     path('genres/', views.genre_list, name='genres_list'),
     path('authors/', views.author_list, name='authors_list'),
     path('songs/', views.song_list, name='songs_list'),
     path('playlists/', views.playlist_list, name='playlists_list'),
     path('albums/', views.album_list, name='albums_list'),
     path('genres/<int:pk>', views.genre_detail, name='genre_detail'),
     path('authors/<int:pk>', views.author_detail, name='author_detail'),
     path('songs/<int:pk>', views.song_detail, name='song_detail'),
     path('playlists/<int:pk>', views.playlist_detail, name='playlist_detail'),
     path('albums/<int:pk>', views.album_detail, name='album_detail'),
     path('profile/', views.profile, name='profile'),
     path('editprofile/', views.edit_profile, name='edit_profile'),
     path('likesong/<int:pk>', views.like_song, name='like_song'),
     path('likealbum/<int:pk>', views.like_album, name='like_album'),
     path('likeplaylist/<int:pk>', views.like_playlist, name='like_playlist'),
     path('deleteplaylist/<int:pk>', views.delete_playlist, name='delete_playlist'),
     path('createplaylist/', views.create_playlist, name='create_playlist'),
     path('deletesong/<int:pk1>/<int:pk2>', views.delete_song_from_playlist, name='delete_song_from_playlist'),
     path('search/', views.search, name='search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
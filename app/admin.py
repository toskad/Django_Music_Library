from django.contrib import admin
from .models import *

admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Album)
admin.site.register(Playlist)
admin.site.register(Song)
admin.site.register(UserProfile)

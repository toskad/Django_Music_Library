from django.forms import ModelForm
from django import forms
from .models import *


class PlaylistForm(ModelForm):
    class Meta:
         model = Playlist
         fields = ['author','title','text','image']

    def __init__(self, user, *args, **kwargs):
        super(PlaylistForm, self).__init__(*args, **kwargs)
        self.fields['author'].initial = UserProfile.objects.filter(pk = user.id)


class SongForm(forms.Form):
    playlist = forms.ModelChoiceField(Playlist.objects.all())

    def __init__(self, user, *args, **kwargs):
        super(SongForm, self).__init__(*args, **kwargs)
        self.fields['playlist'].queryset = Playlist.objects.filter(author = user.id)


class UserImageForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']

    def __init__(self, *args, **kwargs):
        super(UserImageForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False


class UserEditForm(ModelForm):
    class Meta:
        model = User
        fields = ['username']

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.fields['username'].required = False


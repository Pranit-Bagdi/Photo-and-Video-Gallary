from django import forms
from .models import Album,Photo,Video


class AlbumForm(forms.ModelForm):
    class Meta:
        model=Album
        fields=('title','album_image')

class PhotoForm(forms.ModelForm):
    class Meta:
        model=Photo
        fields=('album','image','lable')

    def __init__(self, user, *args, **kwargs):
        super(PhotoForm, self).__init__(*args, **kwargs)
        self.fields['album'].queryset = Album.objects.filter(user=user)
        
class VideoForm(forms.ModelForm):
    class Meta:
        model=Video
        fields=('album','caption','video')   
    
    def __init__(self, user, *args, **kwargs):
        super(VideoForm, self).__init__(*args, **kwargs)
        self.fields['album'].queryset = Album.objects.filter(user=user)         
  
  

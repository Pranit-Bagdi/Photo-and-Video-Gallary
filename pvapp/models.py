from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe
from .validators import file_size
# Album
class Album(models.Model):
    album_image=models.ImageField(upload_to="album_img/",null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    status=models.BooleanField(default=True)
    date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' % (self.album_image.url))

# PhotosVideoModel
class Photo(models.Model):
    album=models.ForeignKey(Album, on_delete=models.CASCADE,null=True)
    image=models.ImageField(upload_to="photos/")
    date=models.DateTimeField(auto_now_add=True)
    lable=models.CharField(max_length=100)
    
    def __str__(self):
        return self.lable
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="80"/>' %(self.image.url))

class Video(models.Model):
    album=models.ForeignKey(Album, on_delete=models.CASCADE,null=True)
    caption=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)
    video=models.FileField(upload_to="Video/%y",validators=[file_size])
    
    def __str__(self):
        return self.caption
from django.contrib import admin
from . import models
from .models import Video,Album,Photo
# Register your models here.

class AlbumAdmin(admin.ModelAdmin):
	list_display=('title','date','image_tag','user')
admin.site.register(models.Album,AlbumAdmin)

class PhotoAdmin(admin.ModelAdmin):
	list_display=('lable','date','image_tag','album')
admin.site.register(models.Photo,PhotoAdmin)

admin.site.register(Video)
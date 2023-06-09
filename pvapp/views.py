from django.shortcuts import render,redirect
from .models import Album,Photo,Video
from django.db.models import Count
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# UserSignup
# Form
from .forms import AlbumForm,PhotoForm,VideoForm

# Create your views here.
def home(request):
    data=Album.objects.annotate(total_photos=Count('photo')).filter(status=True)
    return render(request,'home.html',{'data':data})

#Photos List
def photos(request,album_id):
    album=Album.objects.get(id=album_id)
    data=Photo.objects.filter(album=album)
    return render(request,'photos-list.html',{'data':data,'album':album})

# Video List
def videos(request,album_id):
    album=Album.objects.get(id=album_id)
    data=Video.objects.filter(album=album)
    return render(request,'video-list.html',{'data':data,'album':album})


# SIgnUp
def signup(request):
    msg=''
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            msg='Thanks for signup'
    form=UserCreationForm
    return render(request,'registration/signup.html',{'form':form,'msg':msg})

#Dashboard
@login_required
def dashboard(request):
    totalAlbums=Album.objects.filter(user=request.user).count()
    totalPhotos=Photo.objects.filter(album__user=request.user).count()
    totalVideos=Video.objects.filter(album__user=request.user).count()
    print(totalVideos)
    return render(request,'dashboard.html',{'totalAlbums':totalAlbums,'totalPhotos':totalPhotos,'totalVideos':totalVideos})

# UserAlbums  {% url 'update-album' album.id %}
@login_required
def user_albums(request):
   data=Album.objects.annotate(total_photos=Count('photo')).filter(user=request.user)
   return render(request,'user-album-list.html',{'data':data})


# Video List in Album
@login_required
def video_albums(request):
   data=Album.objects.annotate(total_video=Count('video')).filter(user=request.user)
   return render(request,'video-album-list.html',{'data':data})



@login_required
def add_album(request):
    msg=''
    if request.method=='POST':
        form=AlbumForm(request.POST,request.FILES)
        if form.is_valid():
            saveForm=form.save(commit=False)
            saveForm.user=request.user
            saveForm.save()
            msg='Data has been added'
    form=AlbumForm
    return render(request,'add-album.html',{'form':form,'msg':msg})

@login_required
def update_album(request,id):
    album=Album.objects.get(id=id)
    msg=''
    if request.method=='POST':
        form=AlbumForm(request.POST,request.FILES,instance=album)
        if form.is_valid():
            saveForm=form.save(commit=False)
            saveForm.user=request.user
            saveForm.save()
            msg='Data has been updated'
    form=AlbumForm(instance=album)
    return render(request,'update-album.html',{'form':form,'msg':msg})

@login_required
def delete_album(request,id):
    Album.objects.filter(id=id).delete()
    return redirect('user-albums')

@login_required
def photo_list(request,album_id):
    album=Album.objects.get(id=album_id)
    photos=Photo.objects.filter(album=album)
    return render(request,'user-photo-list.html',{'data':photos,'album':album})

@login_required
def video_list(request,album_id):
    album=Album.objects.get(id=album_id)
    videos=Video.objects.filter(album=album)
    return render(request,'user-video-list.html',{'data':videos,'album':album})


@login_required
def add_photo(request,album_id):
    album=Album.objects.get(id=album_id)
    msg=''
    if request.method=='POST':
        form=PhotoForm(request.user,request.POST,request.FILES)
        if form.is_valid():
            saveForm=form.save(commit=False)
            saveForm.save()
            msg='Data has been added'
            return redirect('/photo-list/'+str(album_id))
    form=PhotoForm(request.user)
    return render(request, 'add-photo.html',{'form':form,'msg':msg,'album':album})


@login_required
def add_video(request,album_id):
    album=Album.objects.get(id=album_id)
    print(album)
    msg=''
    if request.method=='POST':
        form=VideoForm(request.user,request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            msg='Data has been added'
            return redirect('/video-list/'+str(album_id))
    form=VideoForm(request.user)
    return render(request, 'add-video.html',{'form':form}) 

@login_required
def delete_photo(request,album_id,photo_id):
    Photo.objects.filter(id=photo_id).delete()
    return redirect('/photo-list/'+str(album_id))

@login_required
def delete_video(request,album_id,video_id):
    Video.objects.filter(id=video_id).delete()
    return redirect('/video-list/'+str(album_id))

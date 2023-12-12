from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from my_music_app.web_my_music_app.forms import AlbumCreateForm, AlbumEditForm, AlbumDeleteForm, ProfileCreateForm
from my_music_app.web_my_music_app.models import Profile, Album


def get_profile():
    return Profile.objects.first()


def home_page(request):
    profile = get_profile()
    albums = Album.objects.all()

    if not profile:
        return redirect('create profile')

    context = {
        'profile': profile,
        'albums': albums,
    }

    return render(request, 'core/home-with-profile.html', context)


def add_album(request):
    if request.method == "GET":
        form = AlbumCreateForm()
    else:
        form = AlbumCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
    }

    return render(request, 'album/add-album.html', context)


def details_album(request, pk):
    album = Album.objects.filter(pk=pk).get()

    context = {
        'album': album,
    }

    return render(request, 'album/album-details.html', context)


def edit_album(request, pk):
    album = Album.objects.filter(pk=pk).get()

    if request.method == "GET":
        form = AlbumEditForm(instance=album)
    else:
        form = AlbumEditForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'album': album,
        'form': form,
    }

    return render(request, 'album/edit-album.html', context)


def delete_album(request, pk):
    album = Album.objects.filter(pk=pk).get()

    if request.method == "GET":
        form = AlbumDeleteForm(instance=album)
    else:
        album.delete()
        return redirect('home page')

    context = {
        'form': form,
        'album': album,
    }

    return render(request, 'album/delete-album.html', context)


def create_profile(request):

    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
    }
    return render(request, 'core/home-no-profile.html', context)


def details_profile(request):
    profile = get_profile()
    count_album = Album.objects.count()

    context = {
        'profile': profile,
        'count_album': count_album,
    }

    return render(request, 'profile/profile-details.html', context)


def delete_profile(request):
    profile = get_profile()
    albums = Album.objects.all()

    if request.method == 'POST':
        profile.delete()
        albums.delete()

        return redirect('home page')

    return render(request, 'profile/profile-delete.html')

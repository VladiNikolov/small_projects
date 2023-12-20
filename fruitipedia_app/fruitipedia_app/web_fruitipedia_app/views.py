from django.shortcuts import render, redirect

from fruitipedia_app.web_fruitipedia_app.forms import ProfileCreateForm, ProfileEditForm, FruitCreateForm, \
    FruitEditForm, FruitDeleteForm
from fruitipedia_app.web_fruitipedia_app.models import Profile, Fruit


def get_profile():
    return Profile.objects.first()


def home_page(request):
    profile = get_profile()
    fruits = Fruit.objects.all()

    if not profile:
        return redirect('create profile')

    context = {
        'profile': profile,
        'fruits': fruits,
    }

    return render(request, 'core/index.html', context)


def dashboard_page(request):
    profile = get_profile()
    fruits = Fruit.objects.all()

    context = {
        'profile': profile,
        'fruits': fruits,
    }

    return render(request, 'core/dashboard.html', context)


def create_fruit(request):
    if request.method == 'GET':
        form = FruitCreateForm()
    else:
        form = FruitCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard page')

    context = {
        'form': form,
    }

    return render(request, 'fruit/create-fruit.html', context)


def details_fruit(request, pk):
    fruits = Fruit.objects.filter(pk=pk).get()

    context = {
        'fruits': fruits,
    }

    return render(request, 'fruit/details-fruit.html', context)


def edit_fruit(request, pk):
    fruits = Fruit.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = FruitEditForm(instance=fruits)
    else:
        form = FruitEditForm(request.POST, instance=fruits)
        if form.is_valid():
            form.save()
            return redirect('dashboard page')

    context = {
        'form': form,
        'fruits': fruits,
    }

    return render(request, 'fruit/edit-fruit.html', context)


def delete_fruit(request, pk):
    fruits = Fruit.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = FruitDeleteForm(instance=fruits)
    else:
        fruits.delete()
        return redirect('dashboard page')

    context = {
        'form': form,
        'fruits': fruits,
    }

    return render(request, 'fruit/delete-fruit.html', context)


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
        'hide_nav_links': True,
    }

    return render(request, 'profile/create-profile.html', context)


def details_profile(request):
    profile = get_profile()
    post_count = Fruit.objects.count()

    context = {
        'profile': profile,
        'post_count': post_count,
    }

    return render(request, 'profile/details-profile.html', context)


def edit_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'form': form,
    }

    return render(request, 'profile/edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    fruits = Fruit.objects.all()

    if request.method == 'POST':
        profile.delete()
        fruits.delete()

        return redirect('home page')

    return render(request, 'profile/delete-profile.html')

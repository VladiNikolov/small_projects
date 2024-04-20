from django.shortcuts import render, redirect

from world_of_speed_app_last.car.models import Car
from world_of_speed_app_last.profile_name.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from world_of_speed_app_last.web.views import get_profile


def create_profile(request):
    profile = get_profile()

    form = CreateProfileForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('catalogue page')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profile/profile-create.html', context)


def details_profile(request):
    profile = get_profile()
    cars = Car.objects.all()
    total_sum = sum(car.price for car in cars)

    context = {
        'profile': profile,
        'cars': cars,
        'total_sum': total_sum,
    }

    return render(request, 'profile/profile-details.html', context)


def edit_profile(request):
    profile = get_profile()

    form = EditProfileForm(instance=profile)
    if request.method == 'POST':
        form = EditProfileForm(request.POST or None, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profile/profile-edit.html', context)


def delete_profile(request):
    profile = get_profile()

    form = DeleteProfileForm(instance=profile)
    if request.method == 'POST':
        profile.delete()
        return redirect('home_page')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profile/profile-delete.html', context)
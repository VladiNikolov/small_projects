from django.shortcuts import render, redirect, get_object_or_404

from world_of_speed_app_last.car.forms import CreateCarForm, EditCarForm, DeleteCarForm
from world_of_speed_app_last.car.models import Car
from world_of_speed_app_last.profile_name.models import Profile
from world_of_speed_app_last.web.views import get_profile


def catalogue_page(request):
    profile = get_profile()
    cars = Car.objects.all()
    count_cars = Car.objects.count()

    context = {
        'profile': profile,
        'cars': cars,
        'count_cars': count_cars,
    }

    return render(request, 'car/catalogue.html', context)


def create_car(request):
    profile = Profile.objects.first()

    form = CreateCarForm(request.POST)
    if form.is_valid():
        form.instance.owner_id = profile.pk
        form.save()
        return redirect('catalogue page')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'car/car-create.html', context)


def details_car(request, pk):
    profile = get_profile()
    car = get_object_or_404(Car, pk=pk)

    context = {
        'profile': profile,
        'car': car,
    }

    return render(request, 'car/car-details.html', context)


def edit_car(request, pk):
    profile = get_profile()
    car = get_object_or_404(Car, pk=pk)

    form = EditCarForm(instance=car)
    if request.method == 'POST':
        form = EditCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue page')

    context = {
        'profile': profile,
        'car': car,
        'form': form,
    }

    return render(request, 'car/car-edit.html', context)


def delete_car(request, pk):
    car = get_object_or_404(Car, pk=pk)

    if request.method == 'POST':
        car.delete()
        return redirect('home_page')

    form = DeleteCarForm(instance=car)

    context = {
        'profile': Profile.objects.first(),
        'form': form,
    }
    return render(request, 'car/car-delete.html', context)
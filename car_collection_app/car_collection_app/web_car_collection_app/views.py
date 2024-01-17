from django.shortcuts import render, redirect

from car_collection_app.web_car_collection_app.forms import ProfileCreateForm, CarCreateForm, CarEditForm, \
    CarDeleteForm, ProfileEditForm
from car_collection_app.web_car_collection_app.models import Profile, Car


def home_page(request):
    profile = Profile.objects.first()

    if not profile:
        return redirect('create profile')

    context = {
        'profile': profile,
    }

    return render(request, 'core/index.html', context)


def create_profile(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
    }
    return render(request, 'profile/profile-create.html', context)


def catalogue(request):
    cars = Car.objects.all()

    context = {
        'profile': Profile.objects.first(),
        'cars': cars
    }

    return render(request, 'core/catalogue.html', context)


def create_car(request):
    if request.method == 'GET':
        form = CarCreateForm()
    else:
        form = CarCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'profile': Profile.objects.first(),
        'form': form,
    }

    return render(request, 'car/car-create.html', context)


def details_car(request, pk):
    profile = Profile.objects.first(),
    car = Car.objects.get(id=pk)

    context = {
        'profile': profile,
        'car': car,
    }
    return render(request, 'car/car-details.html', context)


def edit_car(request, pk):
    profile = Profile.objects.first(),
    car = Car.objects.get(id=pk)

    if request.method == "GET":
        form = CarEditForm(instance=car)
    else:
        form = CarEditForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'car': car,
        'profile': profile,
    }

    return render(request, 'car/car-edit.html', context)


def delete_car(request, pk):
    profile = Profile.objects.first()
    car = Car.objects.get(id=pk)

    if request.method == 'GET':
        form = CarDeleteForm(instance=car)
    else:
        form = CarDeleteForm(request.POST, instance=car)
        car.delete()
        return redirect('catalogue')

    context = {
        'form': form,
        'car': car,
        'profile': profile,
    }

    return render(request, 'car/car-delete.html', context)


def details_profile(request):
    profile = Profile.objects.first()
    all_cars = Car.objects.all()

    total_sum = sum(car.price for car in all_cars)

    context = {
        'profile': profile,
        'total_sum': total_sum
    }

    return render(request, 'profile/profile-details.html', context)


def edit_profile(request):
    profile = Profile.objects.first()

    if request.method == "GET":
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profile/profile-edit.html', context)


def delete_profile(request):
    profile = Profile.objects.first()
    cars = Car.objects.all()

    if request.method == 'POST':
        profile.delete()
        cars.delete()
        return redirect('home page')

    context = {
        'profile': profile,
    }

    return render(request, 'profile/profile-delete.html', context)




from django.shortcuts import render, redirect

from eventer_app.web_eventer_app.forms import ProfileCreateForm, ProfileEditForm, EventCreateForm, EventEditForm
from eventer_app.web_eventer_app.models import Profile, Event


def home_page(request):
    profile = Profile.objects.first()

    if not profile:
        return redirect('create profile')

    context = {
        'profile': profile,
    }
    return render(request, 'shared/home-page.html', context)


def dashboard_page(request):
    events = Event.objects.all()

    context = {
        'profile': Profile.objects.first(),
        'events': events
    }
    return render(request, 'events/dashboard.html', context)


def create_event(request):
    if request.method == "GET":
        form = EventCreateForm()
    else:
        form = EventCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard page')

    context = {
        'form': form,
        'profile': Profile.objects.first(),
    }

    return render(request, 'events/event-create.html', context)


def details_event(request, pk):
    profile = Profile.objects.first()
    event = Event.objects.get(id=pk)

    context = {
        'profile': profile,
        'event': event,
    }

    return render(request, 'events/events-details.html', context)


def edit_event(request, pk):
    profile = Profile.objects.first()
    event = Event.objects.get(id=pk)

    if request.method == "GET":
        form = EventEditForm(instance=event)
    else:
        form = EventEditForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('dashboard page')

    context = {
        'profile': profile,
        'event': event,
        'form': form,
    }

    return render(request, 'events/event-edit.html', context)


def delete_event(request, pk):
    profile = Profile.objects.first()
    event = Event.objects.get(id=pk)

    if request.method == 'POST':
        profile.delete()
        event.delete()
        return redirect('home page')

    context = {
        'profile': profile,
        'event': event,
    }

    return render(request, 'events/events-delete.html', context)


def create_profile(request):
    if request.method == "GET":
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard page')

    context = {
        'form': form,
    }

    return render(request, 'profiles/profile-create.html', context)


def details_profile(request):
    profile = Profile.objects.first()
    count_events = Event.objects.count()

    context = {
        'profile': profile,
        'count_events': count_events,
    }

    return render(request, 'profiles/profile-details.html', context)


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
        'form': form,
        'profile': profile,
    }

    return render(request, 'profiles/profile-edit.html', context)


def delete_profile(request):
    profile = Profile.objects.first()
    events = Event.objects.all()

    if request.method == 'POST':
        profile.delete()
        events.delete()
        return redirect('home page')

    context = {
        'profile': profile,
    }
    return render(request, 'profiles/profile-delete.html', context)

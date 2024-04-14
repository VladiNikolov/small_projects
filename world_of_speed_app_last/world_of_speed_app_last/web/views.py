from django.shortcuts import render

from world_of_speed_app_last.profile_name.models import Profile


def get_profile():
    return Profile.objects.first()


def home_page(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }

    return render(request, 'core/index.html', context)
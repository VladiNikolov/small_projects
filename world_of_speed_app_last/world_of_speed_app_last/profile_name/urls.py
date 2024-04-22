from django.urls import path

from world_of_speed_app_last.profile_name.views import create_profile, details_profile, edit_profile, delete_profile

urlpatterns = (
    path('create/', create_profile, name='create profile'),
    path('details/', details_profile, name='details profile'),
    path('edit/', edit_profile, name='edit profile'),
    path('delete/', delete_profile, name='delete profile'),
)
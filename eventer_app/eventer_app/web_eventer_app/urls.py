from django.urls import path

from eventer_app.web_eventer_app.views import home_page, dashboard_page, create_event, details_event, edit_event, \
    delete_event, create_profile, details_profile, edit_profile, delete_profile

urlpatterns = (
    path('', home_page, name='home page'),
    path('dashboard/', dashboard_page, name='dashboard page'),
    path('create/', create_event, name='create event'),
    path('details/<int:pk>/', details_event, name='details event'),
    path('edit/<int:pk>/', edit_event, name='edit event'),
    path('delete/<int:pk>/', delete_event, name='delete event'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/details/', details_profile, name='details profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
)
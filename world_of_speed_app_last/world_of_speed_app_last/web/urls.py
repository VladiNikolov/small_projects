from django.urls import path

from world_of_speed_app_last.web.views import home_page

urlpatterns = (
    path('', home_page, name='home_page'),
)
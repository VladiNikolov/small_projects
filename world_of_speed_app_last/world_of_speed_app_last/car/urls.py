from django.urls import path

from world_of_speed_app_last.car.views import catalogue_page, create_car, details_car, edit_car, delete_car

urlpatterns = (
    path('catalogue/', catalogue_page, name='catalogue page'),
    path('create/', create_car, name='create car'),
    path('<int:pk>/details/', details_car, name='details car'),
    path('<int:pk>/edit/', edit_car, name='edit car'),
    path('<int:pk>/delete/', delete_car, name='delete car'),
)

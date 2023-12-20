""""
•	http://localhost:8000/ - index page
•	http://localhost:8000/dashboard/ - dashboard page
•	http://localhost:8000/create/ - fruit create page
•	http://localhost:8000/<fruitId>/details/ - fruit details page
•	http://localhost:8000/<fruitId>/edit/ - fruit edit page
•	http://localhost:8000/<fruitId>/delete/ - fruit delete page
•	http://localhost:8000/profile/create/ - profile create page
•	http://localhost:8000/profile/details/ - profile details page
•	http://localhost:8000/profile/edit/ - profile edit page
•	http://localhost:8000/profile/delete/ - profile delete page

"""
from django.urls import path

from fruitipedia_app.web_fruitipedia_app.views import home_page, dashboard_page, create_fruit, details_fruit, \
    edit_fruit, delete_fruit, create_profile, details_profile, edit_profile, delete_profile

urlpatterns = (
    path('', home_page, name='home page'),
    path('dashboard/', dashboard_page, name='dashboard page'),
    path('create/', create_fruit, name='create fruit'),
    path('<int:pk>/details/', details_fruit, name='details fruit'),
    path('<int:pk>/edit/', edit_fruit, name='edit fruit'),
    path('<int:pk>/delete/', delete_fruit, name='delete fruit'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/details/', details_profile, name='details profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
)
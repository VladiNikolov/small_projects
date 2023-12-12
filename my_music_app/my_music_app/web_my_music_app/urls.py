""""
•	http://localhost:8000/ - home page
•	http://localhost:8000/album/add/ - add album page
•	http://localhost:8000/album/details/<id>/ - album details page
•	http://localhost:8000/album/edit/<id>/ - edit album page
•	http://localhost:8000/album/delete/<id>/ - delete album page
•	http://localhost:8000/profile/details/ - profile details page
•	http://localhost:8000/profile/delete/ - delete profile page

"""
from django.urls import path

from my_music_app.web_my_music_app.views import home_page, add_album, details_album, edit_album, delete_album, \
    create_profile, details_profile, delete_profile

urlpatterns = (
    path('', home_page, name='home page'),
    path('album/add/', add_album, name='add album'),
    path('album/details/<int:pk>/', details_album, name='details album'),
    path('album/edit/<int:pk>/', edit_album, name='edit album'),
    path('album/delete/<int:pk>/', delete_album, name='delete album'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/details/', details_profile, name='details profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
)
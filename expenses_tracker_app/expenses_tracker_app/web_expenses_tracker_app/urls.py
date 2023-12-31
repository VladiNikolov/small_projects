""""
•	http://localhost:8000/ - home page
•	http://localhost:8000/create/ - create expense page
•	http://localhost:8000/edit/<id>/ - edit expense page
•	http://localhost:8000/delete/<id>/ - delete expense page
•	http://localhost:8000/profile/ - profile page
•	http://localhost:8000/profile/edit/ - profile edit page
•	http://localhost:8000/profile/delete/ - delete profile page

"""
from django.urls import path

from expenses_tracker_app.web_expenses_tracker_app.views import home_page, create_expense, edit_expense, delete_expense, \
    details_profile, edit_profile, delete_profile, create_profile

urlpatterns = (
    path('', home_page, name='home page'),
    path('create/', create_expense, name='create expense'),
    path('edit/<int:pk>/', edit_expense, name='edit expense'),
    path('delete/<int:pk>/', delete_expense, name='delete expense'),

    path('profile/create/', create_profile, name='create_profile'),
    path('profile/', details_profile, name='details profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
)
from django.contrib import admin

from car_collection_app.web_car_collection_app.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "age")
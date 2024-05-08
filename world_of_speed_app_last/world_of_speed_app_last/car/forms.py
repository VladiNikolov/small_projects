from django import forms
from django.forms import models

from world_of_speed_app_last.car.models import Car


class CreateCarForm(models.ModelForm):
    class Meta:
        model = Car
        exclude = ('owner',)

    widgets = {
        'image_url': forms.URLInput(
            attrs={'placeholder': "https://..."}
        )
    }
    error_messages = {
        'image_url': {
            'unique': "This image URL is already in use! Provide a new one.",
        }
    }


class EditCarForm(models.ModelForm):
    class Meta:
        model = Car
        exclude = ('owner',)

        labels = {
            'image_url': "Image URL",
        }


class DeleteCarForm(models.ModelForm):
    class Meta:
        model = Car
        exclude = ('owner',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'



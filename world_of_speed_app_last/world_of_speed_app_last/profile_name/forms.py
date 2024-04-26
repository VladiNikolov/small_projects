from django import forms
from django.forms import models

from world_of_speed_app_last.profile_name.models import Profile


class CreateProfileForm(models.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age', 'password')

        widgets = {
            'password': forms.PasswordInput(),
        }
        help_texts = {
            'age': "Age requirement: 21 years and above.",
        }


class EditProfileForm(models.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfileForm(models.ModelForm):
    class Meta:
        model = Profile
        fields = ()

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for (_, field) in self.fields.items():
    #         field.widget.attrs['disabled'] = 'disabled'
    #         field.widget.attrs['readonly'] = 'readonly'

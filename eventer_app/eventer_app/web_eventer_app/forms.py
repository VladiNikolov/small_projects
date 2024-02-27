from django import forms

from eventer_app.web_eventer_app.models import Profile, Event


class ProfileCreateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('email', 'profile_picture', 'password')


class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'profile_picture', 'password')


class EventCreateForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('__all__')


class EventEditForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('__all__')

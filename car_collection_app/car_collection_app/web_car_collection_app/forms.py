from django import forms

from car_collection_app.web_car_collection_app.models import Profile, Car


class ProfileCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ('username', 'email', 'age', 'password')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('__all__')


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('__all__')


class CarEditForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('__all__')


class CarDeleteForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'



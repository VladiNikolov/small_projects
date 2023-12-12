from django import forms

from my_music_app.web_my_music_app.models import Profile, Album


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'age': forms.TextInput(attrs={'placeholder': 'Age'})
        }


class AlbumCreateForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'


class AlbumEditForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'


class AlbumDeleteForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'









from django import forms

from fruitipedia_app.web_fruitipedia_app.models import Profile, Fruit


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'password')
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }

        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': '',
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image_url', 'age')
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'image_url'}),
            'age': forms.NumberInput(attrs={'placeholder': 'age'}),
        }

        labels = {
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'image_url': 'Image URL:',
            'age': 'Age:',
        }


class FruitCreateForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = ('name', 'fruit_image_url', 'description', 'nutrition')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fruit Name'}),
            'fruit_image_url': forms.URLInput(attrs={'placeholder': 'Fruit Image URL'}),
            'description': forms.Textarea(attrs={'placeholder': 'Fruit Description'}),
            'nutrition': forms.Textarea(attrs={'placeholder': 'Nutrition Info'}),
        }

        labels = {
            'name': '',
            'fruit_image_url': '',
            'description': '',
            'nutrition': '',
        }


class FruitEditForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = ('name', 'fruit_image_url', 'description', 'nutrition')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fruit Name'}),
            'fruit_image_url': forms.URLInput(attrs={'placeholder': 'Fruit Image URL'}),
            'description': forms.Textarea(attrs={'placeholder': 'Fruit Description'}),
            'nutrition': forms.Textarea(attrs={'placeholder': 'Nutrition Info'}),
        }

        labels = {
            'name': 'Name:',
            'fruit_image_url': 'Image URL:',
            'description': 'Description:',
            'nutrition': 'Nutrition:',
        }


class FruitDeleteForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = ('name', 'fruit_image_url', 'description')
        labels = {
            'name': 'Name:',
            'fruit_image_url': 'Image URL:',
            'description': 'Description:',
        }
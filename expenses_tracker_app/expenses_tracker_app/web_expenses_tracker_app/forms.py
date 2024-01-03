from django import forms

from expenses_tracker_app.web_expenses_tracker_app.models import Profile, Expense


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'profile_image')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'profile_image')


class ExpenseCreateForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title', 'description', 'expense_image', 'price')
        labels = {
            'title': 'Title:',
            'description': 'Description:',
            'expense_image': 'Link to Image:',
            'price': 'Price:'
        }


class ExpenseEditForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title', 'description', 'expense_image', 'price')
        labels = {
            'title': 'Title:',
            'description': 'Description:',
            'expense_image': 'Link to Image:',
            'price': 'Price:'
        }


class ExpenseDeleteForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title', 'description', 'expense_image', 'price')
        labels = {
            'title': 'Title:',
            'description': 'Description:',
            'expense_image': 'Link to Image:',
            'price': 'Price:'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
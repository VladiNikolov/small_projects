from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.utils.deconstruct import deconstructible

""""
•	Profile
    o	First name
        	Character field, required.
        	 It should have at least 2 characters and maximum - 15 characters.
        	The name should consist only of letters. Otherwise, raise ValidationError with the message: "Ensure this value contains only letters."
    o	Last name 
        	Character field, required.
        	It should have at least 2 characters and maximum - 15 characters.
        	The name should consist only of letters. Otherwise, raise ValidationError with the message: "Ensure this value contains only letters."
    o	Budget
        	Float field, required. The budget is 0 by default.
        	The budget should not be below 0, when created or edited.
    o	Profile Image
        	Image field, optional. The picture is user.png (located in the resources) by default; if no image is uploaded)
        	The max size limit is 5MB (inclusive). Otherwise, raise ValidationError with the message: "Max file size is 5.00 MB"
"""


def validate_only_letters(value):
    if not value.isalpha():
        raise ValidationError("Ensure this value contains only letters.")


@deconstructible
class MaxFileSizeInMBValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size
        if filesize > self.max_size * 1024 * 1024:
            raise ValidationError("Max file size is 5.00 MB")


class Profile(models.Model):
    first_name = models.CharField(null=False, blank=False, max_length=15, validators=(MinLengthValidator(2),),)
    last_name = models.CharField(null=False, blank=False, max_length=15, validators=(MinLengthValidator(2),),)
    budget = models.FloatField(null=False, blank=False, default=0, validators=(MinValueValidator(0),),)
    profile_image = models.ImageField(upload_to='profiles/', null=True, blank=True, validators=(MaxFileSizeInMBValidator(5),),)


"""
•	Expense
    o	Title
        	Character field, required.
        	 It should consist of a maximum of 30 characters.
    o	Expense Image
        	URL field, required.
    o	Description
        	Text field, optional.
    o	Price
        	Float field, required.
"""


class Expense(models.Model):
    title = models.CharField(null=False, blank=False, max_length=30)
    expense_image = models.URLField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(null=False, blank=False)
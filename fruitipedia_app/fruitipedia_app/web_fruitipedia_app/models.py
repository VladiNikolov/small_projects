from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

""""
•	Profile Model
o	    First Name
	        Character field, required.
	        It should consist of a maximum of 25 characters and a minimum of 2 characters.
	        The first name must start with a letter. Otherwise raise ValidationError with the following message: "Your name must start with a letter!"
o	    Last Name
	        Character field, required.
	        It should consist of a maximum of 35 characters and a minimum of 1 character.
	        The last name must start with a letter. Otherwise raise ValidationError with the following message: "Your name must start with a letter!"
o	    Email
	        Email field, required.
	        It should consist of a maximum of 40 characters.
o	    Password
	        Character (password) field, required.
	        It should consist of a maximum of 20 characters and a minimum of 8 characters.
o	    Image URL
	        URL field, optional.
o	    Age
	        Integer field, optional.
	        The age default value should be 18.
"""


def validate_first_and_last_name_must_start_whit_letter(value):
    if not value[0].isalpha():
        raise ValidationError("Your name must start with a letter!")


def validate_name_should_contain_only_letters(value):
    if not value.isalpha():
        raise ValidationError("Fruit name should contain only letters!")


class Profile(models.Model):
    first_name = models.CharField(null=False, blank=False, max_length=25, validators=(MinLengthValidator(2), validate_first_and_last_name_must_start_whit_letter,),)
    last_name = models.CharField(null=False, blank=False, max_length=35, validators=(MinLengthValidator(1), validate_first_and_last_name_must_start_whit_letter,),)
    email = models.EmailField(null=False, blank=False, max_length=40)
    password = models.CharField(null=False, blank=False, max_length=20, validators=(MinLengthValidator(8),),)
    image_url = models.URLField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True, default=18)


""""
•	Fruit Model
o	    Name
	        Character field, required.
	        It should consist of a maximum of 30 and a minimum of 2 characters.
	        The name should contain only letters. Otherwise raise a ValidationError with the following message: "Fruit name should contain only letters!"
o	    Image URL
	        URL field, required.
o	    Description
	        Text field, required.
o	    Nutrition
	        Text field, optional.
"""


class Fruit(models.Model):
    name = models.CharField(null=False, blank=False, max_length=30, validators=(MinLengthValidator(2), validate_name_should_contain_only_letters,),)
    fruit_image_url = models.URLField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    nutrition = models.TextField(null=True, blank=True)

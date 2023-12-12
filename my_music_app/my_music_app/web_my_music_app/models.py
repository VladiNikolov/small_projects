from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

# Create your models here.

""""
•	Profile
o	    Username
	        Character field, required.
	        It should have at least 2 characters and maximum - 15 characters.
	        The username can consist only of letters, numbers, and underscore ("_"). Otherwise, raise a ValidationError with the message: "Ensure this value contains only letters, numbers, and underscore."
o	    Email
	        Email field, required.
o	    Age
	        Integer field, optional.
	        The age cannot be below 0.
"""


def validate_only_letters_numbers_and_underscore(value):
    if not value.isalpha() and value.isdigit() and value != '_':
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")


class Profile(models.Model):
    username = models.CharField(null=False, blank=False, max_length=15, validators=(MinLengthValidator(2), validate_only_letters_numbers_and_underscore,),)
    email = models.EmailField(null=False, blank=False)
    age = models.IntegerField(null=True, blank=True, validators=(MinValueValidator(0),),)

""""
•	Album
o	    Album Name
	        Character field, required.
	        All album names must be unique.
	         It should consist of a maximum of 30 characters.
o	    Artist
	        Character field, required.
	        It should consist of a maximum of 30 characters.
o	    Genre
	        Char field, required.
	        It should consist of a maximum of 30 characters.
	        The choices are "Pop Music", "Jazz Music", "R&B Music", "Rock Music", "Country Music", "Dance Music", "Hip Hop Music", and "Other".
o	    Description
	        Text field, optional.
o	    Image URL
	        URL field, required.
o	    Price
	        Float field, required.
	        The number of decimal places of the price should not be specified in the database.
	        The price cannot be below 0.0.
"""


class Album(models.Model):
    CHOICES = (
        ("Pop Music", "Pop Music"),
        ("Jazz Music", "Jazz Music"),
        ("R&B Music", "R&B Music"),
        ("Rock Music", "Rock Music"),
        ("Country Music", "Country Music"),
        ("Dance Music", "Dance Music"),
        ("Hip Hop Music", "Hip Hop Music"),
        ("Other", "Other"),
    )

    album_name = models.CharField(null=False, blank=False, unique=True, max_length=30)
    artist = models.CharField(null=False, blank=False, max_length=30)
    genre = models.CharField(null=False, blank=False, max_length=30, choices=CHOICES)
    description = models.TextField(null=True, blank=True)
    image_url = models.URLField(null=False, blank=False)
    price = models.FloatField(null=False, blank=False, validators=(MinValueValidator(0.0),),)
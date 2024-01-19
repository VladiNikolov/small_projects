from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


def valid_username_length_validator(value):
    if value < 2:
        raise ValidationError("The username must be a minimum of 2 chars")


class Profile(models.Model):
    username = models.CharField(null=False, blank=False, max_length=10, validators=(MinLengthValidator(2, valid_username_length_validator,),),)
    email = models.EmailField(null=False, blank=False)
    age = models.IntegerField(null=False, blank=False, validators=(MinValueValidator(18),),)
    password = models.CharField(null=False, blank=False, max_length=30)
    first_name = models.CharField(null=True, blank=True, max_length=30)
    last_name = models.CharField(null=True, blank=True, max_length=30)
    profile_picture = models.URLField(null=True, blank=True)


def valid_year_validator(value):
    if not 1980 <= value <= 2049:
        raise ValidationError("Year must be between 1980 and 2049")


class Car(models.Model):
    TYPES = (
        ("Sport Car", "Sport Car"),
        ("Pickup", "Pickup"),
        ("Crossover", "Crossover"),
        ("Minibus", "Minibus"),
        ("Other", "Other")
    )

    type = models.CharField(null=False, blank=False, max_length=10, choices=TYPES)
    model = models.CharField(null=False, blank=False, max_length=20, validators=(MinLengthValidator(2),),)
    year = models.IntegerField(null=False, blank=False, validators=(valid_year_validator,),)
    image_url = models.URLField(null=False, blank=False)
    price = models.FloatField(null=False, blank=False, validators=(MinValueValidator(1),),)


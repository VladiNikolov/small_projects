from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
import datetime

def first_name_consist_only_letter(value):
    if not value.isalpha():
        raise ValidationError('The name should contain only letters!')


def password_must_contain_one_digit(value):
    if value.isalpha():
        raise ValidationError("The password must contain at least 1 digit!")


def date_validation(date):
    if date != datetime.date.today():
        print("The date cannot be in the past!")



class Profile(models.Model):
    first_name = models.CharField(blank=False, null=False, max_length=20, validators=(first_name_consist_only_letter,),)
    last_name = models.CharField(blank=False, null=False, max_length=30, validators=(MinLengthValidator(4),),)
    email = models.EmailField(blank=False, null=False, max_length=45)
    profile_picture = models.URLField(blank=True, null=True)
    password = models.CharField(blank=False, null=False, max_length=20, validators=(MinLengthValidator(5), password_must_contain_one_digit,),)


CHOICES = (
    ("Sports", "Sports"),
    ("Festivals", "Festivals"),
    ("Conferences", "Conferences"),
    ("Performing Art", "Performing Art"),
    ("Concerts", "Concerts"),
    ("Theme Party", "Theme Party"),
    ("Other", "Other"),
)


class Event(models.Model):
    event_name = models.CharField(blank=False, null=False, max_length=30, validators=(MinLengthValidator(2),),)
    category = models.CharField(blank=False, null=False, choices=CHOICES)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(blank=False, null=False, validators=(date_validation,),)
    event_image = models.URLField(blank=False, null=False)

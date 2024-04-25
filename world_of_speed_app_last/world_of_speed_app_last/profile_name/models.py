from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

# def validate_length_username(name):
#     if len(name) < 3:
#         raise ValidationError("Username must be at least 3 characters long")


def validate_chars_username(username):
    for ch in username:
        if not ch.isalnum() and ch != '_':
            raise ValidationError("Username must contain only letters, digits, and underscores!")


class Profile(models.Model):
    username = models.CharField(
        null=False,
        blank=False,
        max_length=15,
        validators=(MinLengthValidator(3, message="Username must be at least 3 chars long!",),
                    validate_chars_username),
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        null=False,
        blank=False,
        help_text="Age requirement: 21 years and above.",
    )

    password = models.CharField(
        null=False,
        blank=False,
        max_length=20,
    )

    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=25,
    )

    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=25,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


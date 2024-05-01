from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


def validate_car_year(year):
    if year < 1999 or year > 2030:
        raise ValidationError("Year must be between 1999 and 2030!")


class Car(models.Model):

    CHOICES = (
        ('Rally', 'Rally'),
        ('Open-wheel', 'Open-wheel'),
        ('Kart', 'Kart'),
        ('Drag', 'Drag'),
        ('Other', 'Other'),
    )

    type = models.CharField(
        null=False,
        blank=False,
        max_length=10,
        choices=CHOICES,
    )

    model = models.CharField(
        null=False,
        blank=False,
        max_length=15,
        validators=(MinLengthValidator(1),),
    )

    year = models.IntegerField(
        null=False,
        blank=False,
        validators=(validate_car_year,),
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        unique=True,
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=(MinValueValidator(1.0),),
    )

    owner = models.ForeignKey(
        'profile_name.Profile',
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )
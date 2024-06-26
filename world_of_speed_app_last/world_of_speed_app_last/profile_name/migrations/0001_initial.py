# Generated by Django 4.2.11 on 2024-04-14 08:01

import django.core.validators
from django.db import migrations, models
import world_of_speed_app_last.profile_name.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(3, message='Username must be at least 3 chars long!'), world_of_speed_app_last.profile_name.models.validate_chars_username])),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField(help_text='Age requirement: 21 years and above.')),
                ('password', models.CharField(max_length=20)),
                ('first_name', models.CharField(blank=True, max_length=25, null=True)),
                ('last_name', models.CharField(blank=True, max_length=25, null=True)),
                ('profile_picture', models.URLField(blank=True, null=True)),
            ],
        ),
    ]

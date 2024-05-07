# Generated by Django 4.2.11 on 2024-04-14 08:19

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import world_of_speed_app_last.car.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profile_name', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Rally', 'Rally'), ('Open-wheel', 'Open-wheel'), ('Kart', 'Kart'), ('Drag', 'Drag'), ('Other', 'Other')], max_length=10)),
                ('model', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(1)])),
                ('year', models.IntegerField(validators=[world_of_speed_app_last.car.models.validate_car_year])),
                ('image_url', models.URLField(unique=True)),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(1.0)])),
                ('owner', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='profile_name.profile')),
            ],
        ),
    ]

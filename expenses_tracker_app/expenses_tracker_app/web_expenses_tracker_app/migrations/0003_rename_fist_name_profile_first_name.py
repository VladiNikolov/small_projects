# Generated by Django 4.2.8 on 2023-12-17 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_expenses_tracker_app', '0002_expense'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='fist_name',
            new_name='first_name',
        ),
    ]

# Generated by Django 5.1.4 on 2025-03-10 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_fueltype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carmodel',
            old_name='company',
            new_name='car_company',
        ),
        migrations.RenameField(
            model_name='ceo',
            old_name='company',
            new_name='car_company',
        ),
    ]

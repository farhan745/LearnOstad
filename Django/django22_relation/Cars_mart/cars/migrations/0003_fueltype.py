# Generated by Django 5.1.4 on 2025-01-29 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_carmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='FuelType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('car_models', models.ManyToManyField(to='cars.carmodel')),
            ],
        ),
    ]

# Generated by Django 5.1.4 on 2025-03-05 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_student_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(default=1, upload_to='photos/'),
            preserve_default=False,
        ),
    ]

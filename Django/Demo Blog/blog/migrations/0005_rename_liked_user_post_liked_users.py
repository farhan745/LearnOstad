# Generated by Django 5.1.4 on 2025-02-14 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_liked_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='liked_user',
            new_name='liked_users',
        ),
    ]

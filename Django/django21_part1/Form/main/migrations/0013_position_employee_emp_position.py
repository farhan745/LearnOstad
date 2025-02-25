# Generated by Django 5.1.4 on 2025-01-28 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_rename_name_employee_emp_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Position_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='emp_position',
            field=models.ManyToManyField(blank=True, null=True, to='main.position'),
        ),
    ]

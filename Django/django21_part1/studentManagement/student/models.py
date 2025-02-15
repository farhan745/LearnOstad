from django.db import models
import os


# Create your models here.
def student_directory_name(instance, filename):
    return os.path.join("student/media/", instance.name, filename)


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    checkbox = models.BooleanField(default=False)
    photo = models.ImageField(
        upload_to=student_directory_name, default=None, null=True
    )

    def __str__(self):
        return f"{self.name}"

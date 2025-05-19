from django.db import models
import os
from django.contrib.auth.models import User

def student_directory_name(instance,filename):
    return os.path.join('student/media/',instance.name,filename)
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=10)
    checkbox= models.BooleanField(default=False)
    photo = models.ImageField(upload_to=student_directory_name)
    user = models.ForeignKey(User,null=True, blank=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
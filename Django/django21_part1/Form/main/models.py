from django.db import models

# Create your models here.
class Position(models.Model):
    Position_name = models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return self.Position_name







class Employee(models.Model):
    emp_name = models.CharField(max_length=100)
    emp_salary = models.IntegerField(null=False, blank=False)
    emp_score = models.FloatField(null=True, blank=True)
    emp_email = models.EmailField(null=True, blank=True)
    is_employed = models.BooleanField(default=False, null=True, blank=True)
    # employed_joining_date = models.DateField(null=True, blank=True)#Date field
    employed_joining_date_joined = models.DateTimeField(null=True, blank=True)# Date and Time field
    emp_files = models.FileField(null=True, blank=True,upload_to='files_uploads/')
    emp_profile = models.ImageField(null=True, blank=True,upload_to='emp_profile_pics/')
    emp_url = models.URLField(null=True, blank=True)
    emp_gender = models.CharField(null=True,blank=True,max_length=50)
    password = models.CharField(null=True, blank=True,max_length=36)
    emp_position = models.ManyToManyField(Position, blank=True,null=True)
    def __str__(self):
        return self.emp_name

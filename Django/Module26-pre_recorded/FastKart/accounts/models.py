from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)
    
    def __str__(self):
        self.username
        
        
class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address_line_1 = models.CharField(null=True,blank=True, max_length=100)
    address_line_2 = models.CharField(null=True,blank=True, max_length=100)
    profile_picture = models.ImageField(null=True, blank=True,upload_to='userprofile')
    city = models.CharField(null=True, max_length=100)
    state = models.CharField(blank=True, max_length=100)
    country = models.CharField(blank=True, max_length=100)
    mobile = models.CharField(null=True,blank=True, max_length=20)
    
    def __str__(self):
        return self.user.username
    def full_address(self):
        return f'{self.address_line_1} {self.address_line_2}'
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    
    def __str__(self):
        return self.name
class Tag(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author_id = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category_id=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)# *jodi delete category te null hbe kintu cascade moto delete hbe na
    tag = models.ManyToManyField(Tag,blank=True)
    def __str__(self):
        return self.title 
    
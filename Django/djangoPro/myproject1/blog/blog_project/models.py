from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    created_at = models.DateTimeField()
    extra_fields = models.CharField(max_length=250, null=True)

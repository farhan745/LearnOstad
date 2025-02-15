from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField()
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    tags = models.ManyToManyField(Tag,related_name="posts")
    def __str__(self):
        return self.title


# One to One Relationship
class PostExtraInfo(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    rating = models.FloatField()
    tags = models.JSONField()

# One to Many Relations

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    content = models.TextField()




from django.db import models


# Create your models here.
class Post(models.Model):  # database gele post ekta table
    title = models.CharField(max_length=200)  # title VARCHAR(100)
    content = models.TextField()  # content TEXT
    published = models.BooleanField()  # published BOOLEAN,# html->checkbox
    created_at = models.DateTimeField(
        auto_now_add=True,null=True
    )  # created_at TIMESTAMP #html->input data_time
    updated_at = models.DateTimeField(auto_now=True,null=True)  # updated_at TIMESTAMPpyth

    def __str__(self):
        return self.title

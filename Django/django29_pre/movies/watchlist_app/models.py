from django.db import models
from django.contrib.auth.models import User 
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class MovieList(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    
class Reviews(models.Model):
    #* ekta movie te multiple review takte pare....
    movie = models.ForeignKey(MovieList,on_delete=models.CASCADE,related_name="reviews")
    #* ekta user te multiple review dite pare....
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ])
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.reviewer}->{self.movie.name}"
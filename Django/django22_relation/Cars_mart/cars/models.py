from django.db import models

# Create your models here.
# one to onr

#Car Company and CEO

class CarCompany(models.Model):     #Value ceo then company
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class Ceo(models.Model):
    name = models.CharField(max_length=255) 
    car_company = models.OneToOneField(CarCompany, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
    
#One to Many relationship/////ForeignKey ->One to Many / Many to One
class CarModel(models.Model):
    name = models.CharField(max_length=255)
    car_company = models.ForeignKey(CarCompany, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
#Many to Many
class FuelType(models.Model):
    name = models.CharField(max_length=255)
    car_models = models.ManyToManyField(CarModel)
    def __str__(self):
        return self.name
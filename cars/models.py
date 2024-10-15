from django.db import models
from django.utils import timezone

BRAND_CHOICES = (
    ('MERCEDES', 'Mercedes'),
    ('TESLA', 'Tesla'),
    ('BMW', 'Bmw'),
    ('AUDI', 'Audi')

)
# Create your models here.
class Cars(models.Model):
    care_name = models.CharField(max_length=100)
    car_version = models.CharField(max_length=300)
    car_model = models.CharField(max_length=300)
    brand = models.CharField(max_length=200, choices=BRAND_CHOICES, default='-')
    max_speed = models.PositiveBigIntegerField()
    mix_speed = models.PositiveBigIntegerField(default=0)
    coutry = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('Tag')

class Address(models.Model):
    car = models.OneToOneField(Cars, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)

class FixHistory(models.Model):
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)



class Tag(models.Model):
    name = models.CharField(max_length=255)

    # def __str__(self):
    #     return "{} -{} ".format(self.brand, self.car_model)
        
    # def save(self, *args, **kwargs):
    #     if self.brand == 'Tesla':
    #         self.coutry = 'USA'
    #     else:
    #         self.coutry = 'Germany'
    #     super().save(**args, **kwargs)
        

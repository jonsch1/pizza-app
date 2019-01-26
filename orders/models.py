from django.db import models

# Create your models here.
class Pizza(models.Model):
    name= models.CharField(max_length=64)
    size= models.CharField(max_length=64)
    price= models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name} in {self.size}, costs {self.price} Euro"

class Topping(models.Model):
    name= models.CharField(max_length=64)
    price_small= models.IntegerField(default=1)
    price_large= models.IntegerField(default=2)


    def __str__(self):
        return f"{self.name}"



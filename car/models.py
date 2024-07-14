from django.db import models
from brand.models import Brand
from django.contrib.auth.models import User


# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return self.name + self.description


class Invoice(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return {self.id}


class Comment(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

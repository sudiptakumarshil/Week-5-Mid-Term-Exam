from django.db import models
from brand.models import Brand

# Create your models here.


class Car(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return self.name + self.description

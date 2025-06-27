from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)
    barcode = models.CharField(max_length=50, unique=True)
    calories = models.CharField(max_length=50)
    sugar = models.CharField(max_length=50)
    fat = models.CharField(max_length=50)
    category = models.CharField(max_length=50,default="")
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.name

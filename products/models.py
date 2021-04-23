from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    image = models.ImageField(upload_to='products', height_field=None, width_field=None, max_length=200, 
    null=True)
    featured = models.BooleanField(default=False)
    

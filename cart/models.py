from django.db import models

# Create your models here.


class Cart(models.Model):
    products = models.TextField(blank=True, null=True, max_length=4000)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    custumer = models.CharField(max_length=100)
from django.db import models


class Brand(models.Model):
    name    = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

class Product(models.Model):
    GENDER_PRODUCT = [
        ('M', 'Man'),
        ('W', 'Woman'),
        ('MW', 'Man and Woman'),
    ]

    name        = models.CharField(max_length=255)
    description = models.TextField()
    price       = models.CharField(max_length=255)
    promo       = models.CharField(max_length=255)
    amount      = models.IntegerField()
    brandID     = models.ForeignKey(Brand, on_delete=models.CASCADE)
    gender      = models.CharField(max_length=2, choices=GENDER_PRODUCT)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

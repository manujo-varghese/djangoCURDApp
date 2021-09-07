from django.db import models


# Create your models here.

# class Product with required fields and designed to show product_name when the object is called
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.CharField(max_length=100)
    product_price = models.CharField(max_length=100)
    delivery_price = models.CharField(max_length=100)

    def __str__(self):
        return self.product_name


# class ProductOption designed to have a product (also allows null)
# when product option created without any link to product now
#
class ProductOption(models.Model):
    option_name = models.CharField(max_length=100)
    option_description = models.CharField(max_length=100)
    Product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)

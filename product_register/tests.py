from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import *


# test case created to correctly identify corresponding price for each product
class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(product_name="Shoe", product_description="nike", product_price=200, delivery_price=20)
        Product.objects.create(product_name="T-Shirt", product_description="Adidas", product_price=70, delivery_price=5)

    def test_product_correct_price(self):
        shoe = Product.objects.get(product_name="Shoe")
        t_shirt = Product.objects.get(product_name="T-Shirt")
        self.assertEqual(shoe.product_name, "Shoe")
        self.assertEqual(t_shirt.product_name, "T-Shirt")


# test case created to correctly identify corresponding price for each product_option
class ProductOptionTestCase(TestCase):
    def setUp(self):
        ProductOption.objects.create(option_name="Digital", option_description="digital view")
        ProductOption.objects.create(option_name="Memory", option_description="1 tb memory space")

    def test_product_option_name(self):
        digital = ProductOption.objects.get(option_name="Digital")
        memory = ProductOption.objects.get(option_name="Memory")
        self.assertEqual(digital.option_name, "Digital")
        self.assertEqual(memory.option_name, "Memory")
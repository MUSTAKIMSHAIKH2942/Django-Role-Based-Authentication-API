# products/tests.py

from django.test import TestCase
from products.models import Product

class ProductModelTest(TestCase):

    def test_product_creation(self):
        product = Product.objects.create(
            name="Test Product", description="A test product", price=100.00
        )
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.price, 100.00)

# products/tests_api.py

from rest_framework.test import APITestCase
from rest_framework import status
from products.models import Product

class ProductAPITest(APITestCase):

    def setUp(self):
        self.product_data = {
            "name": "Test Product",
            "description": "Product description",
            "price": 100.0
        }

    def test_create_product(self):
        response = self.client.post('/api/products/', self.product_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_product(self):
        product = Product.objects.create(
            name="Test Product", description="Product description", price=100.0
        )
        response = self.client.get(f'/api/products/{product.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Product')

    def test_update_product(self):
        product = Product.objects.create(
            name="Test Product", description="Product description", price=100.0
        )
        updated_data = {"name": "Updated Product", "price": 120.0}
        response = self.client.put(f'/api/products/{product.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Product')

    def test_delete_product(self):
        product = Product.objects.create(
            name="Test Product", description="Product description", price=100.0
        )
        response = self.client.delete(f'/api/products/{product.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

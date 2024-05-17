from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Product, Order, OrderProduct


class ProductAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.user.is_staff = True
        self.user.save()
        self.client.force_authenticate(user=self.user)
        self.product_url = reverse('product-list')

    def test_create_product(self):
        data = {"name": "Product1", "price": "19.99"}
        response = self.client.post(self.product_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, "Product1")

    def test_get_products(self):
        Product.objects.create(name="Product1", price="19.99")
        response = self.client.get(self.product_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class OrderAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.client.force_authenticate(user=self.user)
        self.product1 = Product.objects.create(name="Product1", price="19.99")
        self.product2 = Product.objects.create(name="Product2", price="29.99")
        self.order_url = reverse('order-list')

    def test_create_order(self):
        data = {
            "user": self.user.id,
            "products": [self.product1.id, self.product2.id],
            "amounts": ["10.99", "10.99"]
        }
        response = self.client.post(self.order_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        order = Order.objects.get()
        self.assertEqual(order.user, self.user)
        self.assertIn(self.product1, order.products.all())
        self.assertIn(self.product2, order.products.all())

    def test_get_orders(self):
        order = Order.objects.create(user=self.user)
        # order.products.add(self.product1, self.product2)
        OrderProduct.objects.create(
            order=order, product=self.product1, amount=20)
        OrderProduct.objects.create(
            order=order, product=self.product2, amount=42)

        response = self.client.get(self.order_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['user'], self.user.username)
        self.assertEqual(len(response.data[0]['products']), 2)


class APIFailureTest(APITestCase):
    def test_not_found(self):
        response = self.client.get("/api/home/product/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_unauthorized(self):
        response = self.client.get("/api/products/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Product, Order, Payment
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class ProductModelTest(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product", price=9.99)

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.price, 9.99)


class OrderModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.product = Product.objects.create(
            name="Test Product", price=9.99)
        self.order = Order.objects.create(user=self.user)
        self.order.products.add(self.product)

    def test_order_creation(self):
        self.assertEqual(self.order.user.username, 'testuser')
        self.assertIn(self.product, self.order.products.all())


class PaymentModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.product = Product.objects.create(
            name="Test Product", price=9.99)
        self.order = Order.objects.create(user=self.user)
        self.order.products.add(self.product)
        self.payment = Payment.objects.create(order=self.order, amount=9.99)

    def test_payment_creation(self):
        self.assertEqual(self.payment.amount, 9.99)
        self.assertEqual(self.payment.order, self.order)


class ProductAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.client.force_authenticate(user=self.user)
        self.product_url = reverse('product-list')

    def test_create_product(self):
        data = {"name": "Product1", "price": 19.99}
        response = self.client.post(self.product_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, "Product1")

    def test_get_products(self):
        Product.objects.create(name="Product1", price=19.99)
        response = self.client.get(self.product_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class OrderAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.client.force_authenticate(user=self.user)
        self.product = Product.objects.create(name="Product1", price=19.99)
        self.order_url = reverse('order-list')

    def test_create_order(self):
        data = {
            "user": self.user.id,
            "products": [self.product.id]
        }
        response = self.client.post(self.order_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get().user.username, 'testuser')

    def test_get_orders(self):
        order = Order.objects.create(user=self.user)
        order.products.add(self.product)
        response = self.client.get(self.order_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class PaymentAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.client.force_authenticate(user=self.user)
        self.product = Product.objects.create(name="Product1", price=19.99)
        self.order = Order.objects.create(user=self.user)
        self.order.products.add(self.product)
        self.payment_url = reverse('payment-list')

    def test_create_payment(self):
        data = {
            "order": self.order.id,
            "amount": 19.99
        }
        response = self.client.post(self.payment_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Payment.objects.count(), 1)
        self.assertEqual(Payment.objects.get().amount, 19.99)

    def test_get_payments(self):
        Payment.objects.create(order=self.order, amount=19.99)
        response = self.client.get(self.payment_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

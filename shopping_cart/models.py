from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class OrderStatus(models.TextChoices):
    INITIATED = 'initiated', 'Initiated'
    PENDING = 'pending', 'Pending'
    COMPLETED = 'completed', 'Completed'
    CANCELLED = 'cancelled', 'Cancelled'


class PaymentStatus(models.TextChoices):
    INITIATED = 'initiated', 'Initiated'
    SUCCESS = 'success', 'Success'
    FAILED = 'failed', 'Failed'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through="OrderProduct")
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending', choices=[(
        OrderStatus.value, OrderStatus.name) for OrderStatus in OrderStatus])

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)


class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, default='initiated', choices=[(
        PaymentStatus.value, PaymentStatus.name) for PaymentStatus in PaymentStatus])

    def __str__(self):
        return f"Payment for Order {self.order.id}"

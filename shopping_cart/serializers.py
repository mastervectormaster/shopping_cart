from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Order, Payment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'amount']

class OrderSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Order
        fields = ['id', 'products', 'user', 'created_at', 'status']

    def create(self, validated_data):
        products_data = validated_data.pop('products')
        order = Order.objects.create(user=self.context['request'].user)
        order.products.set(products_data)
        return order

class PaymentSerializer(serializers.ModelSerializer):
    order = OrderSerializer()

    class Meta:
        model = Payment
        fields = ['id', 'order', 'amount', 'payment_date', 'status']

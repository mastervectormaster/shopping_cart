from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from .models import Product, Order, Payment, OrderProduct
from .serializers import ProductSerializer, OrderSerializer, PaymentSerializer, UserSerializer
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib.auth.hashers import make_password

User = get_user_model()


def addAmount(order):
    orderWithAmounts = order
    print(order)
    amounts = [item.amount for item in OrderProduct.objects.filter(
        order_id=order['id'])]
    orderWithAmounts['amounts'] = amounts
    return orderWithAmounts


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

    @action(detail=True, methods=['post'], permission_classes=[IsAdminUser])
    def increase_amount(self, request, pk=None):
        print(request.user)
        product = self.get_object()
        amount = request.data.get('amount', 0.00)
        product.amount += int(amount)
        product.save()
        return Response({'status': 'amount increased'})


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        # do your thing here
        amounts = request.data.get('amounts')
        order = Order.objects.create(user=request.user)

        for index, product in enumerate(request.data.get('products')):
            OrderProduct.objects.create(
                product=Product.objects.get(id=product), order=order, amount=amounts[index])
            print(product)
        return Response({'status': 'order added'}, status=status.HTTP_201_CREATED)

    def list(self, request):
        response = map(addAmount, super().list(request).data)
        return Response(list(response))

    @action(detail=True, methods=['post'])
    def add_product(self, request, pk=None):
        order = self.get_object()
        product_id = request.data.get('product')
        amount = request.data.get('amount')
        product = Product.objects.get(id=product_id)
        OrderProduct.objects.create(
            product=product, order=order, amount=amount)
        return Response({'status': 'product added to order'})

    @action(detail=True, methods=['post'])
    def remove_product(self, request, pk=None):
        order = self.get_object()
        print(order)
        product_id = request.data.get('product')
        orderProduct = OrderProduct.objects.get(
            order_id=order.id, product_id=product_id)
        orderProduct.delete()
        # OrderProduct.objects.create(
        #     product=product, order=order, amount=amount)
        return Response({'status': 'product removed from order'})

    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        order = self.get_object()
        order.status = 'cancelled'
        order.save()
        return self.get_object


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'], permission_classes=[permissions.AllowAny])
    def finalize(self, request, pk=None):
        payment = self.get_object()
        status = request.data.get('status')
        payment.status = status
        payment.save()
        return Response({'status': 'payment finalized'})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'], permission_classes=[permissions.AllowAny])
    def signup(self, request):
        data = request.datadad
        user = User.objects.create_user(
            username=data['username'],
            password=data['password'],
            email=data['email']
        )
        user.save()
        return Response({'status': 'user created'})

    @action(detail=False, methods=['post'], permission_classes=[permissions.AllowAny])
    def login(self, request):
        data = request.data
        user = authenticate(
            username=data['username'], password=data['password'])
        if user is not None:
            login(request, user)
            return Response({'status': 'user logged in'})
        else:
            return Response({'status': 'invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def change_email(self, request):
        user = request.user
        user.email = request.data['email']
        user.save()
        return Response({'status': 'email changed'})

    @action(detail=False, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def change_password(self, request):
        user = request.user
        user.set_password(request.data['password'])
        user.save()
        return Response({'status': 'password changed'})

    @action(detail=False, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def logout(self, request):
        user = request.user
        if user is not None:
            logout(request, user)
            return Response({'status': 'user logged out'})
        else:
            return Response({'status': 'invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

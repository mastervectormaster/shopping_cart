
from django.urls import path
from .views import RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import ProductListApiView
from .views import ProductDetailApiView

urlpatterns = [
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/register/', RegisterView.as_view(), name="sign_up"),
    path('api/auth/user/', RegisterView.as_view(), name="update_user"),
    path('api/product/', ProductListApiView.as_view(), name="product_list" ),
    path('api/product/<int:product_id>/', ProductDetailApiView.as_view(), name="product_detail")
]
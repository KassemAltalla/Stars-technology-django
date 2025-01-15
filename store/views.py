from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import (
    UserProfile, Category, Brand, Product,
    ProductImage, ProductOption, Cart, CartItem,
    Order, OrderItem
)
from .serializers import (
    UserProfileSerializer, CategorySerializer, BrandSerializer,
    ProductSerializer, CartSerializer, OrderSerializer
)

# عرض وتعديل بروفايل المستخدم
class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.userprofile

# عرض جميع الأقسام
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# عرض جميع المنتجات
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# عرض تفاصيل منتج معين
class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# عرض وتعديل العربة
class CartView(generics.RetrieveUpdateAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart

# عرض وإنشاء الطلبات
class OrderListView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        cart = self.request.user.cart
        order = serializer.save(user=self.request.user)
        for item in cart.items.all():
            OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
        cart.items.all().delete()
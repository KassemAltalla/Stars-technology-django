from rest_framework import serializers
from .models import (
    UserProfile, Category, Brand, Product,
    ProductImage, ProductOption, Cart, CartItem,
    Order, OrderItem
)

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'phone_number', 'address']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'image']

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image']

class ProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOption
        fields = ['id', 'name', 'value']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    options = ProductOptionSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'old_price', 'new_price', 'quantity', 'category', 'brand', 'images', 'options']

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    options = ProductOptionSerializer(many=True, read_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'options']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items']

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    options = ProductOptionSerializer(many=True, read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'options']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'order_number', 'full_name', 'email', 'phone_number', 'address', 'items', 'created_at']
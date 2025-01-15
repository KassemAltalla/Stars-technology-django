from django.db import models

from django.contrib.auth.models import User
from django.db import models
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
    
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)

    def __str__(self):
        return self.name
    

class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    old_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    new_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return f"Image for {self.product.name}"
    

class ProductOption(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='options')
    name = models.CharField(max_length=255)  # مثل "اللون"
    value = models.CharField(max_length=255)  # مثل "أبيض"

    def __str__(self):
        return f"{self.name}: {self.value} for {self.product.name}"
    
    
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart for {self.user.username}"
    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    options = models.ManyToManyField(ProductOption, blank=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in {self.cart.user.username}'s cart"
    
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    order_number = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.order_number} by {self.user.username}"
    
    
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    options = models.ManyToManyField(ProductOption, blank=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order {self.order.order_number}"
    
    
    
